#### 1.浅谈
内存对齐可以加快`cpu` 运行速度,那么对于速度要求高的线性代数库,一般都会有内存对齐的要求, 所以自然而然的 `Eigen` 库也会有内存对齐,这篇文章就看`Eigen` 是如何内存对齐的以及要注意的事项


---
#### 2.Eigen栈上对齐
`Eigen `也是用 `C++11` 提供的 `alignas` 关键字对齐
```C++
// 指定16字节对齐
template <typename T, int Size, int MatrixOrArrayOptions,
          int Alignment = (MatrixOrArrayOptions&DontAlign) ? 0
                        : compute_default_alignment<T,Size>::value >
struct plain_array
{
  T array[Size];
  // ...
};

template <typename T, int Size, int MatrixOrArrayOptions>
struct plain_array<T, Size, MatrixOrArrayOptions, 16>
{
  EIGEN_ALIGN_TO_BOUNDARY(8) T array[Size];
  // ...
};

template <typename T, int Size, int MatrixOrArrayOptions>
struct plain_array<T, Size, MatrixOrArrayOptions, 16>
{
  EIGEN_ALIGN_TO_BOUNDARY(16) T array[Size];
  // ...
};
```

再例如 `Eigen` 自定义的对齐宏模板
```
#define EIGEN_ALIGN_TO_BOUNDARY(n) alignas(n)
```

---
#### 3.库内常见内存对齐
```C++
Eigen::Vector4d // 数组，大小为4*sizeof(double)
Eigen::Matrix4d // 矩阵，大小为16*sizeof(double)
Eigen::Affine3d // 矩阵，大小为4*4*sizeof(double)
Eigen::Quaterniond // 矩阵，大小为4*sizeof(double)
```

这也是说不是所有的`fixed-size`的`Eigen`类型是16字节对齐的，只有大小能被16整除的才会被设置成16字节对齐。例如`Eigen::Vector4d`是16字节对齐的，但`Eigen::Vector3d`不是，它是8字节对齐的。


---
#### 4.不同场景的注意事项
##### 4.1 传参
一定要传实参！！！
```C++
void my_function(Eigen::Vector2d v);   // error --->形参导致内存不对齐


void my_function(const Eigen::Vector2d& v);  // right ---> 实参本身是对齐的
```


##### 4.2 堆上对齐
当 `Eigen` 的类对象作为类内对象时,需要添加宏`EIGEN_MAKE_ALIGNED_OPERATOR_NEW` 来帮助用`new` 时在对上进行内存对齐
```C++
struct Camera {

    EIGEN_MAKE_ALIGNED_OPERATOR_NEW  // 添加宏
    Eigen::Matrix4d param;
};
```

`EIGEN_MAKE_ALIGNED_OPERATOR_NEW` 其实就是 `Eigen` 库自己实现的 `new`和`delete` ,如图
```C++
#define EIGEN_MAKE_ALIGNED_OPERATOR_NEW EIGEN_MAKE_ALIGNED_OPERATOR_NEW_IF(true)
```

该宏将宏 `EIGEN_MAKE_ALIGNED_OPERATOR_NEW_IF(type)` 的 `type` 设置为 `true`,而`EIGEN_MAKE_ALIGNED_OPERATOR_NEW_IF(type)` 宏内容如下 

```C++
  #define EIGEN_MAKE_ALIGNED_OPERATOR_NEW_IF(NeedsToAlign) \
      void *operator new(std::size_t size) { \
        return Eigen::internal::conditional_aligned_malloc<NeedsToAlign>(size); \
      } \
      void *operator new[](std::size_t size) { \
        return Eigen::internal::conditional_aligned_malloc<NeedsToAlign>(size); \
      } \
      void operator delete(void * ptr) EIGEN_NO_THROW { Eigen::internal::conditional_aligned_free<NeedsToAlign>(ptr); } \
      void operator delete[](void * ptr) EIGEN_NO_THROW { Eigen::internal::conditional_aligned_free<NeedsToAlign>(ptr); } \
      void operator delete(void * ptr, std::size_t /* sz */) EIGEN_NO_THROW { Eigen::internal::conditional_aligned_free<NeedsToAlign>(ptr); } \
      void operator delete[](void * ptr, std::size_t /* sz */) EIGEN_NO_THROW { Eigen::internal::conditional_aligned_free<NeedsToAlign>(ptr); } \
      /* in-place new and delete. since (at least afaik) there is no actual   */ \
      /* memory allocated we can safely let the default implementation handle */ \
      /* this particular case. */ \
      static void *operator new(std::size_t size, void *ptr) { return ::operator new(size,ptr); } \
      static void *operator new[](std::size_t size, void* ptr) { return ::operator new[](size,ptr); } \
      void operator delete(void * memory, void *ptr) EIGEN_NO_THROW { return ::operator delete(memory,ptr); } \
      void operator delete[](void * memory, void *ptr) EIGEN_NO_THROW { return ::operator delete[](memory,ptr); } \
      /* nothrow-new (returns zero instead of std::bad_alloc) */ \
      EIGEN_MAKE_ALIGNED_OPERATOR_NEW_NOTHROW(NeedsToAlign) \
      void operator delete(void *ptr, const std::nothrow_t&) EIGEN_NO_THROW { \
        Eigen::internal::conditional_aligned_free<NeedsToAlign>(ptr); \
      } \
      typedef void eigen_aligned_operator_new_marker_type;
```

定义了由 `Eigen` 的内存配置器帮助实现的 `new` 和 `delete`.

##### 4.3 可变长Eigen对象
除了固定大小的Eigen对象，还有动态大小的，例如MatrixXf。
动态大小的Eigen对象的内存由自己管理和释放，也就是说它的内存申请释放是Eigen已经重构为对齐的malloc，因此不需要指定字节对齐。

##### 4.4 STL容器
标准库的内存配置器时自己 `std::allocator`,并**没有内存对齐**,所以如果用 `STL`容器装在 `Eigen` 对象时要用`Eigen` 的内存配置器 `Eigen::aligned_allocator` ，例如
```C++
std::vector<Eigen::Vector3d,Eigen::aligned_allocator<Eigen::Vector3d>> vecs;
```

##### 4.5 智能指针
`std::make_shared`由于`make_shared`使用的是`::new`因此，不要采用它来给智能指针赋值，而是
```C++
std::shared_ptr<T>(new T(args...))
```

##### 4.6 类指针
Eigen指针并不占用空间，因此包含eigen指针的结构体和类也不需要内存对齐。
```C++
struct example {  
    Eigen::Vector2d* a;  
    int b;
};
```

##### 4.7 Eigen数组
Eigen数组由一整块数组组成，因此需要内存对齐。
```C++
struct example {
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
 
    Eigen::Vector2d a[10];  
    int b;
};

// 或者

struct example {
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
 
    std::array<Eigen::Vector2d, 3> a2;
    int b;
};
```

---
#### 5.案例
```C++
class test{
    public:
    test(){
        p.setZero();
        march_p.setZero();
    }
    // 常量引用传递
    test(const Eigen::Vector3d& _p,const Eigen::Vector3d& _march_p):p(_p),march_p(_march_p){
    }

    void print(){
        std::cout<<"the p : "<< p.transpose()<<std::endl;
        std::cout<<"the march p : "<< march_p.transpose()<<std::endl;
    }

    public:
    // Eigen 内存对齐宏
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    private:
    Eigen::Vector3d p;
    Eigen::Vector3d march_p;
};
```