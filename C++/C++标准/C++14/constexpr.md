相对于`C++11` ,`C++14` 对`constexpr` 少了一些限制,C++11如下
```C++
constexpr int factorial(int n) { // C++14 和 C++11均可
    return n <= 1 ? 1 : (n * factorial(n - 1));
}
```
C++11中constexpr函数必须必须把所有东西都放在一个单独的return语句中，而constexpr则无此限制,C++14如下
```C++
constexpr int factorial(int n) { // C++11中不可，C++14中可以
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        ret += i;
    }
    return ret;
}
```