### 1.安装conda

---
### 2.创建环境并且进入
```shell
## 创建
conda create -n yolov8 python=3.8
## 进入
conda activate yolov8
```

---
### 3.编译环境
到环境目录下
```shell
cd ${yolov8_project_name}
```

设置镜像源
```shell
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
```

安装依赖
```shell
## 项目依赖
pip install -r requirements.txt

## 必要依赖
pip install ultralytics
```

---
### 4.测试
安装预训练模型
yolov8s.pt预训练模型:[yolov8s.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt)
yolov8n.pt预训练模型:[yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)


将下载好的文件放到项目下面,测试用自带文件测试
```shell
yolo predict model=yolov8n.pt source=`ultralytics/assets/bus.jpg`
```

打印为:
```shell
Ultralytics YOLOv8.0.230 🚀 Python-3.8.18 torch-2.1.2+cpu CPU (Intel Core(TM) i7-10750H 2.60GHz)
YOLOv8n summary (fused): 168 layers, 3151904 parameters, 0 gradients, 8.7 GFLOPs

image 1/1 E:\code\python\ultralytics\ultralytics\assets\bus.jpg: 640x480 4 persons, 1 bus, 1 stop sign, 113.8ms
Speed: 8.0ms preprocess, 113.8ms inference, 14.5ms postprocess per image at shape (1, 3, 640, 480)
Results saved to runs\detect\predict4
💡 Learn more at https://docs.ultralytics.com/modes/predict
```

可以看到结果保存到了 `.\runs\detect\predict4`.


---
### 5.训练自己的模型
#### 5.1 `cpu` 版本
在主文件夹下创建 `data` 文件夹,并且创建`data.yaml`文件
```yaml
# 这里需要转成yolov8训练集 
# //xxx/xxx为训练集图片根目录地址，一定要是绝对路径
path:
train: images/train    
val: images/val
test: #(可选)

## 类别
names:
    0:0
    1:1
    ...

```

训练:
```shell
# task:任务类型,可选['detect','segment','classify','init'],不同的task对应不同的参数模型
# mode:模式,可选['train','val','predict']
# data:yaml配置文件
# model:下载的模型，放在主文件下
# epochs:训练轮数
# imagez:训练时ai看到的图片大小，检查大图片建议使用640，小图片可以320 越大越吃性能
# batch:一轮训练中每一次放入图片数量，越大越快效果越好，但是对性能要求越高
# device:使用的设备，使用cpu练就写cpu，使用显卡大多数都是0，多显卡就0，1，2，3，...多少显卡往后写多少

yolo train data=data/data.yaml model=yolov8n.pt epochs=300 imgsz=640 batch=8 workers=0 device=cpu
```


#### 5.2 `gpu` 版本
安装 `torch` 的 `cuda` 版本的来训练,然后进行训练

```shell
yolo train data=data/data.yaml model=yolov8s.pt epochs=300 imgsz=640 batch=8 workers=0 device=0
```

其中 `device` 中有多个`gpu`,可以写为`device=0,1,2,...`



#### 5.3 训练和标签说明
data文件夹下的数据排列为
```
data
    |-- train
    |   |-- images
    |        |-- xx1.jpg
    |        |-- xx2.jpg
    |        ...
    |   |-- labels
    |        |-- xx1.txt
    |        |-- xx2.txt
    |        ...
    |-- val
        |-- images
             |-- xx1.jpg
             |-- xx2.jpg
             ...
        |-- labels
             |-- xx1.txt
             |-- xx2.txt
             ...
```



```shell
## 安装yolov8源码包
## 创建
conda create -n yolov8 python=3.8
## 进入
conda activate yolov8
## 转移到 yolov8环境空间
cd ${yolov8_project_name}
## 设置镜像源
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
## 添加库
## 项目依赖
pip install -r requirements.txt
## 必要依赖
pip install ultralytics
```