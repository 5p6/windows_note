#### 1.参数
* task:任务类型,可选['detect','segment','classify','init'],不同的task对应不同的参数模型
* mode:模式,可选['train','val','predict']
* data:yaml配置文件
* model:下载的模型，放在主文件下
* epochs:训练轮数
* imagez:训练时ai看到的图片大小，可选[640,320]
* batch:一轮训练中每一次放入图片数量，越大越快效果越好，但是对性能要求越高，最好是 2 的倍数
* device:使用的设备，使用cpu练就写cpu，使用显卡大多数都是0，多显卡就0，1，2，3，...多少显卡往后写多少

### 2.示例
```shell
1.用学习率 lr = 0.01 和预训练参数model=yolov8n.pt训练十轮
        yolo train data=data/data.yaml model=yolov8n.pt epochs=10 batch=8 imgsz=640 lr0=0.01 device=cpu
2.预测
        yolo predict model=yolov8n-seg.pt source='https://youtu.be/LNwODJXcvt4' imgsz=320
3.验证
        yolo val model=yolov8n.pt data=coco128.yaml batch=1 imgsz=640
4.导出onnx
        yolo export model=yolov8n-cls.pt format=onnx imgsz=224,128 opset=12
```

### 3.帮助命令
```
yolo help
yolo checks
yolo version
yolo settings
yolo copy-cfg
yolo cfg
```