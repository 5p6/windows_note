#### 1 古典编译模式
```shell 
mkdir build && cd build
cmake .. -DCAMKE_BUILD_TYPE=Release 
make -j 8
make install
```

创建一个`build`文件夹,进入`build`文件夹中然后开始编译.


---
#### 2 现代编译模式
##### 2.1 基础
```shell
cmake -S . -B build
cmake --build build
```

第一行命令指定编译的目录为 `build`(`-B`) ,如果没有的话就会创建一个,而指定编译的`CMakeLists.txt` 文件的目录为 `.`(`-S`) 即当前目录.
然后第二行命令指定编译(`--build`)的后的文件(cmake缓存,可执行文件,动态/静态库)放在 `build` 文件夹中,可以不指定编译器类型,会自动使用编译器.

##### 2.2 指定编译器
指定编译器
```shell
CC=clang CXX=clang++ cmake -S . -B build
```

(推荐)编译器工具可以通过 `cmake --help` 查看,同时可以使用 `-G "your tool"` 来指定工具链,例如
```shell
# msvc工具链
cmake -S . -B build -G "Visual Studio 17 2022"
# linux 工具链
cmake -S . -B build -G "Unix Makefiles"
```



##### 2.3 选项
同时你还可以使用 `-D` 来设置单个选项, `-L` 设设置一列选项,`-LH` 用来可读的帮助,例如
```shell
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
```

##### 2.4 执行
a.添加调试信息
在执行命令后添加 `-v`(`--verbose`) ,即可使得执行编译时添加调试信息.
```shell
cmake --build . -v
```
b.添加编译类型
在执行命令后添加 `--config Debug/Release/RelWithDebInfo` ,即可使得执行编译时添加调试信息.
```shell
cmake --build . --config Release
```

##### 2.5 安装
在编译后通过 `install` 将库和`.cmake` 相关的文件安装
a.基础版
```shell
cmake --install .
```

b.进阶版
```shell
cmake --install . --prefix ${pre_name}
```

`--prefix` 选项后面可以选择 `install` 的前缀文件夹,等效为
```shell
## 预编译
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=${pre_name}

## 生成
cmake --build . --config release

## 安装
cmake --install .
```

##### 2.6 常见选项
* CMAKE_BUILD_TYPE:从Release、RelWithDebInfo、Debug中选择，有时甚至更多。, or sometimes more.
* CMAKE_INSTALL_PREFIX: 要安装到的位置。UNIX上的系统安装通常是/usr/local（默认值），用户目录通常是~/.local，或者您可以选择一个文件夹.
* BUILD_SHARED_LIBS: 您可以将此设置为ON或OFF以控制共享库的默认值（不过，作者可以显式地选择其中一个与另一个，而不是使用默认值）
* BUILD_TESTING: 这是启用测试的常用名称，但并非所有包都使用它，有时是有充分理由的.
* CMAKE_CXX_STANDARD:C++特性标准.
