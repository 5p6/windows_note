### 1.launch文件作用
主要用于启动多个节点

### 2.使用方法
流程:
* 在 `${pkg_name}` 下创建一个 `launch` 文件夹
* 创建 `xxx.launch` 文件
* 编辑launch文件内容,例如
```html

<launch>
    <node pkg="helloworld" type="demo_hello" name="hello" output="screen" />
    <node pkg="turtlesim" type="turtlesim_node" name="t1"/>
    <node pkg="turtlesim" type="turtle_teleop_key" name="key1" />
</launch>
```
* 运行
  * `roslaunch ${pkg_name} xxx.launch`

### 3.launch 文件标签
包括十一种标签
|`<launch>`|`<node>`|`<machine>`|`<include>`|
|---|---|---|---|
|`<remap>`|`<env>`|`<param>`|`<rosparam>`|
|`<group>`|`<test>`|`<arg>`||

* `<launch>`:该标签是任何`roslaunch`文件的根元素。 其唯一目的是充当其他元素的容器。
* `<node>`:最常见的标签，用于启动和关闭节点。`roslaunch`不保证节点开始的顺序。所以无法从外部知道何时完全初始化节点，所有启动的代码都必须能够按任意顺序启动。
* `<machine>`:该标签声明了可以在其上运行ROS节点的计算机。 如果要在本地启动所有节点，则不需要此标记。 它主要用于声明远程计算机的SSH和ROS环境变量设置，但你也可以使用它来声明有关本地计算机的信息。具体属性请参考machine标签。
* `<include>`:该标签可以将另一个`roslaunch` XML文件导入当前文件。 它将被导入到文档的当前范围内，包括`<group>`和`<remap>`标记。 除`<master>`标记外，将导入引用文件中的所有内容：`<master>`标签仅在顶级文件中服从。
* `<remap>`:节点重映射，用于改变节点订阅或发布的话题。
  * 比如
```
<remap from="/different_topic" to="/needed_topic"/>
```

* `<env>`:该标签允许你在启动的节点上设置环境变量。 此标签只能在`<launch>`，`<include>`，`<node>`或`<machine>`标签的范围内使用。 在`<launch>`标签内使用它时，`<env>`标记仅适用于之后声明的节点。 在Environment Variables中可以找到这些环境变量。
* `<param>`:该标签定义要在参数服务器上设置的参数。你可以将`<param>`标记放在`<node>`标记内，在这种情况下，该参数被视为私有参数。
  * 比如
```
<param name="publish_frequency" type="double" value="10.0" />
```
* `<rosparam>`:该标签允许使用`rosparam`YAML文件从ROS参数服务器加载和转储参数。 它也可以用来删除参数。 可以将`<rosparam>`标记放在`<node>`标记内，在这种情况下，该参数被视为私有名称。
* `<group>`:该标签有利益将设置应用到一组节点。 它具有ns属性，可让您将节点放入单独的名称空间。
* `<test>`:该标签在语法上与`<node>`标签相似。它们都指定要运行的ROS节点，但是`<test>`标签指示该节点实际上是要运行的测试节点。有关这些测试节点的更多信息，请参见rostest文档。
* `<arg>`:该标签允许在命令行、多个文件中传递参数。


### 4.node标签参数
|参数|意义|
|---|---|
|`pkg`|包名|
|`type`|节点类型|
| `name` |节点名称|
|`args` |节点的命令行参数(可选)|
|`machine` |指定机器(可选)|
|`respawn`|如果退出,则自动重新节点(可选),可以为`true,false`|
|`respawn_delay` |上一个条件为`true`时,该项为等待时间|
|` required`|如果节点死亡,则kill掉整个launch|
|`ns`|在${ns} 名称空间中启动节点|
|`output`|节点输出,选择有 `log,screen`,一个是日志,一个是屏幕|