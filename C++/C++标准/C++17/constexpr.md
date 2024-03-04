### 1.
传统的if-else语句是在执行期进行条件判断与选择的，因而在泛型编程中，无法使用if-else语句进行条件判断，比如下面的代码就无法通过编译
```C++
template<typename T> inline
int print(T x){
    if(std::is_same<int,T>::value)
        std::cout<<"int value type"<<std::endl;
        return x;
    else
        static_cast<int>(x);
}
```

报错如下
```shell
E:\code\C++\test\example.cpp(122,1): error C2181: 没有匹配 if 的非法 else [E:\code\C++\test\build\example.vcxproj]
```

需要用比较恶心的`std::enable_if`分开讨论，
```C++
// 输入为 int
template<typename T> inline
std::enable_if_t<std::is_same_v<T,int>,int> print(T x){
    return x;
}

// 输入为非 int
template<typename T> inline
std::enable_if_t<!std::is_same_v<T,int>,int> print(T x){
    return static_cast<int>(x);
}
```

上面虽然可以运行,但是十分的不优雅,而且丑陋,所以在 C++17 时引入 `if constexpr`,如下
```C++
// 输入为 int
template<typename T> inline
int print(T x){
    if constexpr(std::is_same<T,int>::value){
        return x;
    } else {
        return static_cast<int>(x);
    }
}
```

如此优雅.