### 1.powershell无法启动虚拟环境
在 `powershell` 中无法启动 `conda` 的虚拟环境,我们在命令行中执行
```shell
conda init --all
```

如果打开`powershell` 发现红色报错,则用**管理员权限** 打开`powershell`,然后输入
```shell
Set-ExecutionPolicy RemoteSigned
```

再输入 `Y` 即可.在新打开的`powershell`界面中我们发现左方就有`conda`  的 `base` 环境.
```shell
(base) PS E:\note>
```