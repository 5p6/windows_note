#### 1.语法
```C++
[ capture-list ] ( params ) mutable(optional) constexpr(optional)(c++17) exception
attribute -> ret { body }


// 可选的简化语法
[ capture-list ] ( params ) -> ret { body } 
[ capture-list ] ( params ) { body } 
[ capture-list ] { body }
```
* capture-list：捕捉列表，这个不⽤多说，前⾯已经讲过，它不能省略；
* params：参数列表，可以省略（但是后⾯必须紧跟函数体）；
* mutable：可选，将 lambda 表达式标记为 mutable 后，函数体就可以修改传值⽅式捕获的变ᰁ
* constexpr：可选， C++17 ，可以指定 lambda 表达式是⼀个常函数；
* exception：可选，指定 lambda 表达式可以抛出的异常；
* attribute：可选，指定 lambda 表达式的特性；
* ret：可选，返回值类型；
* body：函数执⾏体。