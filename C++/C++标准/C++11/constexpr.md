constexpr是c++11新添加的特征，目的是将运算尽量放在编译阶段，而不是运行阶段。
constexpr可以修饰函数、结构体，作用就是加快速度。
* 修饰的函数只能包括return 
* 语句修饰的函数只能引用全局不变常量
* 修饰的函数只能调用其他constexpr修饰的函数
* 函数不能为void 类型和，并且prefix operation（v++）不允许出现。

示例代码:
第一种,最为静态参数
```C++
constexpr int N = 10;
void func(){
    int a[N]; // 不会报错
}
```


第二种,作为返回值
```C++
#include <iostream>
#include <time.h>
using namespace std; 

//在这个函数里面，由于constexpr稀释的是fib1这个函数，因此每一次计算的结果都会作为一个常量保存下来
//这个实现的复杂度等同于迭代的方法，基本上为O(n)。
constexpr long int fib1(int n) 
{ 
	return (n <= 1)? n : fib1(n-1) + fib1(n-2); //只能包含一个retrun语句
} 


//熟悉递归函数就不难证明下面这个函数的时间复杂度为O(2^n)
long int fib2(int n){
        return (n <= 1)? n : fib2(n-1) + fib2(n-2); 
}
int main () 
{ 
	// value of res is computed at compile time. 
  	clock_t start, end;
  	start = clock();
	const long int res_1 = fib1(30); 
  	end = clock();
  	cout << "Totle Time fib1 : " <<(double)(end - start) / CLOCKS_PER_SEC << "s" << endl;
  	start = clock();
	const long int res_2 = fib2(30); 
  	end = clock();
  	cout << "Totle Time fib2 : " <<(double)(end - start) / CLOCKS_PER_SEC << "s" << endl;
	return 0; 
}
```