### 1.内存泄漏
C++编程中,内存泄漏和内存溢出是导致大部分程序错误的原因,其中
* 内存泄漏 指的是程序在申请内存申请后,没有及时释放
* 内存溢出 指程序在申请内存时，没有足够的内存空间供其使用

内存检测工具中 `valgrind`来实现内存检查的情况比较多，这里介绍一种更加便利的内存检测工具， 那就是gcc自带的`sanitizer`。
### 2.sanitizer基本用法
Sanitizers 是谷歌发起的开源工具集，包括AddressSanitizer，MemorySanitizer, ThreadSanitizer, LeakSanitizer, Sanitizers项目本身是llvm项目的一部分，
gcc自带的工具， gcc从4.8版本开始支持Address和Thread Sanitizer，4.9版本开始支持Leak Sanitizer和UBSanitizer。
其中sanitizer支持的内存检测有:
* Use after free 访问对上释放后的内存
* Heap buffer overflow 堆缓冲区溢出
* Stack buffer overflow 栈缓冲区溢出
* Global buffer overflow 全局缓冲区一次
* Use after return 访问栈上释放后的内存
* Use after scope 访问栈上超过范围的内存
* Initialization order bugs 初始化命令错误
* Memory leaks 内存泄漏

使用时只需要在 `CMakeLists.txt` 加入以下内容即可
```Cmake
set(CMAKE_CXX_FLAGS "-g -fsanitize=leak -fsanitize=address -fno-omit-frame-pointer")                    
```

其中
* fsanitize=address 使能Address Sanitizer工具
* fsanitize=leak 只使能Leak Sanitizer，检测内存泄漏问题
* fno-omit-frame-pointer 检测到内存错误时打印函数调用栈
* O1 代码优化选项，可以打印更清晰的函数调用栈


### 3.代码案例
所有代码使用的 `CMakeLists.txt` 的内容都如下
```Cmake
cmake_minimum_required(VERSION 3.10)
project(test)

# 标志
set(CMAKE_CXX_FLAGS "-g -fsanitize=leak -fsanitize=address -fno-omit-frame-pointer")      

# 
add_executable(main main.cc)
```

#### 3.1 案例一：释放已经释放的内存
代码
```C++
int main(int argc,char* argv[]){
    int* p = new int(10);
    int* ptr = p;

    // std::cout<<"* (p + 1)"<< *(p + 1)<<std::endl;
    delete p;
    delete ptr;
    return 0;
}
```

执行后的报告为
```shell {.line-numbers}
=================================================================
==18092==ERROR: AddressSanitizer: attempting double-free on 0x602000000010 in thread T0:
    #0 0x7feb350b724f in operator delete(void*, unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cpp:172
    #1 0x563dccae331a in main /home/robot/code/C++/test/main.cc:14
    #2 0x7feb34829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #3 0x7feb34829e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #4 0x563dccae31c4 in _start (/home/robot/code/C++/test/build/main+0x21c4)

0x602000000010 is located 0 bytes inside of 4-byte region [0x602000000010,0x602000000014)
freed by thread T0 here:
    #0 0x7feb350b724f in operator delete(void*, unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cpp:172
    #1 0x563dccae3304 in main /home/robot/code/C++/test/main.cc:13
    #2 0x7feb34829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

previously allocated by thread T0 here:
    #0 0x7feb350b61e7 in operator new(unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cpp:99
    #1 0x563dccae32a5 in main /home/robot/code/C++/test/main.cc:9
    #2 0x7feb34829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: double-free ../../../../src/libsanitizer/asan/asan_new_delete.cpp:172 in operator delete(void*, unsigned long)
```

注意:
* `SUMMARY` 给出总结为 `double-free`
* `freed`给出首次释放的调用堆栈和行数
* `ERROR` 给出报错的调用堆栈和行数

#### 3.2 案例二：越界检查
C++代码
```C++
#include <iostream>

int main() {
    // 创建一个动态分配的数组，但没有释放内存
    int* array = new int[10];

    // 对数组进行写入操作，超出了数组的边界
    for (int i = 0; i <= 10; ++i) {
        array[i] = i;
    }

    // 释放内存
    delete[] array;

    return 0;
}
```

执行的后检查报告
```shell {.line-numbers}
=================================================================
==18376==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x604000000038 at pc 0x555f3c5b72f8 bp 0x7ffd73d87860 sp 0x7ffd73d87850
WRITE of size 4 at 0x604000000038 thread T0
    #0 0x555f3c5b72f7 in main /home/robot/code/C++/test/main.cc:9
    #1 0x7f5647c29d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f5647c29e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x555f3c5b71c4 in _start (/home/robot/code/C++/test/build/main+0x11c4)

0x604000000038 is located 0 bytes to the right of 40-byte region [0x604000000010,0x604000000038)
allocated by thread T0 here:
    #0 0x7f56484b6357 in operator new[](unsigned long) ../../../../src/libsanitizer/asan/asan_new_delete.cpp:102
    #1 0x555f3c5b729e in main /home/robot/code/C++/test/main.cc:5
    #2 0x7f5647c29d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/robot/code/C++/test/main.cc:9 in main
Shadow bytes around the buggy address:
  0x0c087fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c087fff8000: fa fa 00 00 00 00 00[fa]fa fa fa fa fa fa fa fa
  0x0c087fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==18376==ABORTING
```

注意:
* `SUMMARY` 给出总结为 `heap-buffer-overflow` 即堆缓冲区溢出
* `ERROR` 给出报错的调用堆栈和行数

#### 3.3 案例三：多线程竞争
C++代码
```C++
#include <iostream>
#include <thread>
#include <vector>

// 全局变量，多个线程会同时访问
int global_value = 0;

void increment_global(int n) {
    for (int i = 0; i < n; ++i) {
        // 同时对全局变量进行递增操作
        ++global_value;
    }
}

int main() {
    constexpr int num_threads = 4;
    constexpr int iterations = 100000;

    std::vector<std::thread> threads;

    // 创建多个线程，并让它们同时递增全局变量
    for (int i = 0; i < num_threads; ++i) {
        threads.emplace_back(increment_global, iterations);
    }

    // 等待所有线程结束
    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "Global value: " << global_value << std::endl;

    return 0;
}

```

执行后的检查报告
```shell
==================
WARNING: ThreadSanitizer: data race (pid=19028)
  Read of size 4 at 0x557a41cdb154 by thread T2:
    #0 increment_global(int) /home/robot/code/C++/test/main.cc:11 (main+0x24bc)
    #1 void std::__invoke_impl<void, void (*)(int), int>(std::__invoke_other, void (*&&)(int), int&&) /usr/include/c++/11/bits/invoke.h:61 (main+0x4e68)
    #2 std::__invoke_result<void (*)(int), int>::type std::__invoke<void (*)(int), int>(void (*&&)(int), int&&) /usr/include/c++/11/bits/invoke.h:96 (main+0x4d4e)
    #3 void std::thread::_Invoker<std::tuple<void (*)(int), int> >::_M_invoke<0ul, 1ul>(std::_Index_tuple<0ul, 1ul>) /usr/include/c++/11/bits/std_thread.h:259 (main+0x4c4a)
    #4 std::thread::_Invoker<std::tuple<void (*)(int), int> >::operator()() /usr/include/c++/11/bits/std_thread.h:266 (main+0x4bd2)
    #5 std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(int), int> > >::_M_run() /usr/include/c++/11/bits/std_thread.h:211 (main+0x4b84)
    #6 <null> <null> (libstdc++.so.6+0xdc252)

  Previous write of size 4 at 0x557a41cdb154 by thread T1:
    #0 increment_global(int) /home/robot/code/C++/test/main.cc:11 (main+0x24d4)
    #1 void std::__invoke_impl<void, void (*)(int), int>(std::__invoke_other, void (*&&)(int), int&&) /usr/include/c++/11/bits/invoke.h:61 (main+0x4e68)
    #2 std::__invoke_result<void (*)(int), int>::type std::__invoke<void (*)(int), int>(void (*&&)(int), int&&) /usr/include/c++/11/bits/invoke.h:96 (main+0x4d4e)
    #3 void std::thread::_Invoker<std::tuple<void (*)(int), int> >::_M_invoke<0ul, 1ul>(std::_Index_tuple<0ul, 1ul>) /usr/include/c++/11/bits/std_thread.h:259 (main+0x4c4a)
    #4 std::thread::_Invoker<std::tuple<void (*)(int), int> >::operator()() /usr/include/c++/11/bits/std_thread.h:266 (main+0x4bd2)
    #5 std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(int), int> > >::_M_run() /usr/include/c++/11/bits/std_thread.h:211 (main+0x4b84)
    #6 <null> <null> (libstdc++.so.6+0xdc252)

  Location is global 'global_value' of size 4 at 0x557a41cdb154 (main+0x000000008154)

  Thread T2 (tid=19032, running) created by main thread at:
    #0 pthread_create ../../../../src/libsanitizer/tsan/tsan_interceptors_posix.cpp:969 (libtsan.so.0+0x605b8)
    #1 std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)()) <null> (libstdc++.so.6+0xdc328)
    #2 void __gnu_cxx::new_allocator<std::thread>::construct<std::thread, void (&)(int), int const&>(std::thread*, void (&)(int), int const&) /usr/include/c++/11/ext/new_allocator.h:162 (main+0x363e)
    #3 void std::allocator_traits<std::allocator<std::thread> >::construct<std::thread, void (&)(int), int const&>(std::allocator<std::thread>&, std::thread*, void (&)(int), int const&) /usr/include/c++/11/bits/alloc_traits.h:516 (main+0x311f)
    #4 void std::vector<std::thread, std::allocator<std::thread> >::_M_realloc_insert<void (&)(int), int const&>(__gnu_cxx::__normal_iterator<std::thread*, std::vector<std::thread, std::allocator<std::thread> > >, void (&)(int), int const&) /usr/include/c++/11/bits/vector.tcc:449 (main+0x3253)
    #5 std::thread& std::vector<std::thread, std::allocator<std::thread> >::emplace_back<void (&)(int), int const&>(void (&)(int), int const&) /usr/include/c++/11/bits/vector.tcc:121 (main+0x2cde)
    #6 main /home/robot/code/C++/test/main.cc:23 (main+0x2557)

  Thread T1 (tid=19031, finished) created by main thread at:
    #0 pthread_create ../../../../src/libsanitizer/tsan/tsan_interceptors_posix.cpp:969 (libtsan.so.0+0x605b8)
    #1 std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)()) <null> (libstdc++.so.6+0xdc328)
    #2 void __gnu_cxx::new_allocator<std::thread>::construct<std::thread, void (&)(int), int const&>(std::thread*, void (&)(int), int const&) /usr/include/c++/11/ext/new_allocator.h:162 (main+0x363e)
    #3 void std::allocator_traits<std::allocator<std::thread> >::construct<std::thread, void (&)(int), int const&>(std::allocator<std::thread>&, std::thread*, void (&)(int), int const&) /usr/include/c++/11/bits/alloc_traits.h:516 (main+0x311f)
    #4 void std::vector<std::thread, std::allocator<std::thread> >::_M_realloc_insert<void (&)(int), int const&>(__gnu_cxx::__normal_iterator<std::thread*, std::vector<std::thread, std::allocator<std::thread> > >, void (&)(int), int const&) /usr/include/c++/11/bits/vector.tcc:449 (main+0x3253)
    #5 std::thread& std::vector<std::thread, std::allocator<std::thread> >::emplace_back<void (&)(int), int const&>(void (&)(int), int const&) /usr/include/c++/11/bits/vector.tcc:121 (main+0x2cde)
    #6 main /home/robot/code/C++/test/main.cc:23 (main+0x2557)

SUMMARY: ThreadSanitizer: data race /home/robot/code/C++/test/main.cc:11 in increment_global(int)
==================
Global value: 231884
ThreadSanitizer: reported 1 warnings
```

注意:
* `SUMMARY` 给出总结为 `data race` 即数据竞争
* `ERROR` 给出报错的调用堆栈和行数

#### 3.4 案例四：栈溢出
C++代码
```C++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int func0(void) {
    char str[4];
    strcpy(str, "1234");
    printf("%s \n",str);
    return 0;
}

int main(int argc, char *argv[]) {
    func0();
    return 0;
}
```

执行后的检查报告为
```shell
=================================================================
==20013==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff8d2ce7f4 at pc 0x7f763203a2c3 bp 0x7fff8d2ce7c0 sp 0x7fff8d2cdf68
WRITE of size 5 at 0x7fff8d2ce7f4 thread T0
    #0 0x7f763203a2c2 in __interceptor_memcpy ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:827
    #1 0x55b204045321 in func0() /home/robot/code/C++/test/main.cc:7
    #2 0x55b2040453b1 in main /home/robot/code/C++/test/main.cc:13
    #3 0x7f7631829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #4 0x7f7631829e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #5 0x55b204045184 in _start (/home/robot/code/C++/test/build/main+0x1184)

Address 0x7fff8d2ce7f4 is located in stack of thread T0 at offset 36 in frame
    #0 0x55b204045258 in func0() /home/robot/code/C++/test/main.cc:5

  This frame has 1 object(s):
    [32, 36) 'str' (line 6) <== Memory access at offset 36 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:827 in __interceptor_memcpy
Shadow bytes around the buggy address:
  0x100071a51ca0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51cb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51cc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51cd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51ce0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x100071a51cf0: 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1[04]f3
  0x100071a51d00: f3 f3 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51d10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51d20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51d30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100071a51d40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==20013==ABORTING
```

注意:
* `SUMMARY` 给出总结为 `stack-buffer-overflow` 即栈上缓冲区溢出
* `Address` 给出报错行数
* `ERROR` 给出报错的调用堆栈和行数

同时注意 `str` 只有最后一位是 `0` ,如果复制 `1234` 则 `str` 的size需要 $5$ 个字节.

#### 3.5 案例五：释放后访问
```C++ {.line-numbers}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func2(void) {
    // 申请
    int * a = (int*)malloc(sizeof(int)*1);
    *a = 3;
    printf("a : %d \n",*a);
    // 释放
    free(a);
    // 数据释放后访问
    *a = 1;
    printf("a : %d \n",*a);
}

int main(int argc, char *argv[]) {
    func2();
    return 0;
}
```

运行时的检查报告
```shell
=================================================================
==20399==ERROR: AddressSanitizer: heap-use-after-free on address 0x602000000010 at pc 0x55c8295b72e3 bp 0x7fff4fb79970 sp 0x7fff4fb79960
WRITE of size 4 at 0x602000000010 thread T0
    #0 0x55c8295b72e2 in func2() /home/robot/code/C++/test/main.cc:10
    #1 0x55c8295b7323 in main /home/robot/code/C++/test/main.cc:15
    #2 0x7fd2f9829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #3 0x7fd2f9829e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #4 0x55c8295b7164 in _start (/home/robot/code/C++/test/build/main+0x1164)

0x602000000010 is located 0 bytes inside of 4-byte region [0x602000000010,0x602000000014)
freed by thread T0 here:
    #0 0x7fd2fa0b4537 in __interceptor_free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:127
    #1 0x55c8295b72ab in func2() /home/robot/code/C++/test/main.cc:9
    #2 0x55c8295b7323 in main /home/robot/code/C++/test/main.cc:15
    #3 0x7fd2f9829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

previously allocated by thread T0 here:
    #0 0x7fd2fa0b4887 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x55c8295b723e in func2() /home/robot/code/C++/test/main.cc:6
    #2 0x55c8295b7323 in main /home/robot/code/C++/test/main.cc:15
    #3 0x7fd2f9829d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-use-after-free /home/robot/code/C++/test/main.cc:10 in func2()
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==20399==ABORTING
```

注意:
* `SUMMARY` 给出总结为 `heap-use-after-free` 即栈上缓冲区溢出
* `freed` 给出报错行数和代码
* `ERROR` 给出报错的调用堆栈和行数
