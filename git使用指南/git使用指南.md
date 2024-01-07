## 一.快速入门
### 1.生成标识和邮箱
调用 "git-bash.exe"
``` C++ {.line-numbers}
//code
git config --global user.name "${用户名称}" 
git config --global user.email "${用户邮箱}"
```
### 2.生成 SSH Key 密钥
2.1生成密钥
```C++ {.line-numbers}
//code
ssh-keygen -t rsa -C "${用户邮箱}"
```
1) 路径确认
2) 设置密码和确认密码直接回车键

2.2得到SSH密钥
取到 1)中路径里面找到 `id_rsa.pub` ,用记事本打开,将里面的内容复制即可.

### 3.git保存ssh密钥
3.1点击`github`账号的 `Settings` , 点击 `SSH And GPG keys`
3.2 点击 `New SSH key` ,将 `2.2` 的复制的内容粘贴到`ssh`中 , 生成新的 `SSH` 密钥.

### 4.上传文件
4.1`cd`到上传文件的文件夹中
4.2 git上传文件准备工作
``` C++ {.line-numbers}
git init //初始化本地仓库
    git add ${文件名} //添加一个文件到本地仓库
    git add . //将该目录下的全部文件添加到本地仓库
    git commit -m "${上传时的叙述}"
    git remote add origin ${github库的SSH地址} //关闭远程仓库
    git push -u origin master //将本地仓库文件上传
```


### 附注
* 用户邮箱是github账号注册时的邮箱,而用户名称是github现在的用户名称






笔记仓库
`git@github.com:5p6/note.git`

## 二.记录
### 1.坑
当你在某个文件夹 `git init` 后,如果你后面还要传文件上去,你不必再 `git init` 了,直接 `git add`  和 `git comment` ,并且也不用 `git remote` 来确定远程仓库,直接 `git push` 即可.
`git init` 仅仅是创建`.git` 文件,并且在文件中加入一些必要的东西,所以一次就够了.

### 2.创建分支和递交
```shell
## 创建分支
git branch -M 分支名
## 递交内容
git push -u origin 分支名
```

