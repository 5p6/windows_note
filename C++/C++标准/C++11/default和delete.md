我们知道编译器会为类⾃动⽣成⼀些⽅法，⽐如构造和析构函数现在我们可以显式地指定和禁⽌这些⾃动⾏为了,示例
```C++
struct classA {
 classA() = default; // 声明⼀个⾃动⽣成的函数
 classA(T value);
 void *operator new(size_t) = delete; // 禁⽌⽣成new运算符
}
```