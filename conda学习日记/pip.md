## 常用命令
### 1.管理
```shell
pip list 							#列出当前缓存的包
pip purge 							#清除缓存
pip remove 							#删除对应的缓存
pip help 							#帮助
pip install xxx 					#安装xxx包
pip install xxx.whl					#安装xxx.whl本地包
pip install -r requirements.txt 	#批量安装
pip uninstall xxx 					#删除xxx包
pip show xxx 						#展示指定的已安装的xxx包
pip check xxx 						#检查xxx包的依赖是否合适

```


### 2.设置镜像源
```shell
## 添加镜像源
pip config set global.index-url ${web_name}

## 例如添加镜像源
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
```