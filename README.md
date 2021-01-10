## Label_Transform
该项目可实现将YOLO模型训练所需的txt标签转换成相应的xml格式

`txt标签格式:`

| class_name |  x  |  y  |  w  | h  |
| :---    |:---:|:---:|:---:|---:|
| 8   |0.585 |  0.73067  |0.122|0.3413|
| 8   |  0.416     |  0.84534   |0.176|0.288|


## 代码程序
需要以下环境：

+ python


+ opencv-python


+ lxml


（直接pip install，不用指定版本）

## 开始
将要转换的txt标签对应的图片放入`img`文件夹，txt标签文件放入`txt`文件夹。然后运行`get_list.py`得到转换列表`txt_to_xml_list.txt`。最后运行`txt_to_xml.py`,可以在`xml`文件夹中得到转换化后的xml文件。
