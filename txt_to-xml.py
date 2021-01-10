
from xml.dom.minidom import Document
import os
import os.path
from PIL import Image

def writeXml(tmp, imgname, w, h, objbud, wxml):
    doc = Document()
  
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
   
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode("ImageResource")
    folder.appendChild(folder_txt)
 
    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    filename_txt = doc.createTextNode(imgname)
    filename.appendChild(filename_txt)
    
    path=doc.createElement('path')
    annotation.appendChild(path)
    path_txt=doc.createTextNode(img_path+imgname)
    path.appendChild(path_txt)
    
    source = doc.createElement('source')
    annotation.appendChild(source)
 
    database = doc.createElement('database')
    source.appendChild(database)
    database_txt = doc.createTextNode("Unknown")
    database.appendChild(database_txt)
 
    size = doc.createElement('size')
    annotation.appendChild(size)
 
    width = doc.createElement('width')
    size.appendChild(width)
    width_txt = doc.createTextNode(str(w))
    width.appendChild(width_txt)
 
    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode(str(h))
    height.appendChild(height_txt)
 
    depth = doc.createElement('depth')
    size.appendChild(depth)
    depth_txt = doc.createTextNode("3")
    depth.appendChild(depth_txt)
  
    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    segmented_txt = doc.createTextNode("0")
    segmented.appendChild(segmented_txt)
 
    for i in range(0,len(objbud)//5):
        
        object_new = doc.createElement("object")
        annotation.appendChild(object_new)
 
        name = doc.createElement('name')
        object_new.appendChild(name)
        name_txt = doc.createTextNode(name_list[int(float(objbud[i*5]))])  
        name.appendChild(name_txt)
 
        pose = doc.createElement('pose')
        object_new.appendChild(pose)
        pose_txt = doc.createTextNode("Unspecified")
        pose.appendChild(pose_txt)
 
        truncated = doc.createElement('truncated')
        object_new.appendChild(truncated)
        truncated_txt = doc.createTextNode("0")
        truncated.appendChild(truncated_txt)
 
        difficult = doc.createElement('difficult')
        object_new.appendChild(difficult)
        difficult_txt = doc.createTextNode("0")
        difficult.appendChild(difficult_txt)
        #threes-1#
        bndbox = doc.createElement('bndbox')
        object_new.appendChild(bndbox)
 
        xmin = doc.createElement('xmin')
        bndbox.appendChild(xmin)
        xmin_txt = doc.createTextNode(str(int((float(objbud[i*5+1]) - (float(objbud[i*5+3]))/2)*w + 1)))#
        xmin.appendChild(xmin_txt)
 
        ymin = doc.createElement('ymin')
        bndbox.appendChild(ymin)
        ymin_txt = doc.createTextNode(str(int((float(objbud[i*5+2]) - (float(objbud[i*5+4]))/2)*h + 1)))#
        ymin.appendChild(ymin_txt)
 
        xmax = doc.createElement('xmax')
        bndbox.appendChild(xmax)
        xmax_txt = doc.createTextNode(str(int((float(objbud[i*5+1]) + (float(objbud[i*5+3]))/2)*w + 1)))#
        xmax.appendChild(xmax_txt)
 
        ymax = doc.createElement('ymax')
        bndbox.appendChild(ymax)
        ymax_txt = doc.createTextNode(str(int((float(objbud[i*5+2]) + (float(objbud[i*5+4]))/2)*h + 1)))#
        ymax.appendChild(ymax_txt)
       
    tempfile = tmp + "test.xml"   #
    with open(tempfile, "wb") as f:
        f.write(doc.toprettyxml(indent = '\t', encoding='utf-8'))
 
    rewrite = open(tempfile, "r")
    lines = rewrite.read().split('\n')
    newlines = lines[1:len(lines)-1]
    
    fw = open(wxml, "w")
    for i in range(0, len(newlines)):
        fw.write(newlines[i] + '\n')
    
    fw.close()
    rewrite.close()
    os.remove(tempfile)
    return
 
ann_path = "./RoLabelImg_Transform-master/txt/"  #txt文件路径
img_path = "./RoLabelImg_Transform-master/img/"  #图片路径
xml_path = "./RoLabelImg_Transform-master/xml/"   #xml保存路径
name_list = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable',
'dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']

if not os.path.exists(xml_path):
    os.mkdir(xml_path)
 
for files in os.walk(ann_path):
    temp = "./RoLabelImg_Transform-master/tmp"
    if not os.path.exists(temp):
        os.mkdir(temp)
    for file in files[2]:
        img_name = os.path.splitext(file)[0] + '.jpg'
        fileimgpath = img_path + img_name
        im=Image.open(fileimgpath)  
        width= int(im.size[0])
        height= int(im.size[1])
        
        arr=[] 
        for line in open(ann_path + file):
            for x in line.split(' '):
             arr.append(x)
             obj=arr
        load_arr=list(map(float,arr))

        ob=[str(x) for x in load_arr]  #字符转换
        filename = xml_path + os.path.splitext(file)[0] + '.xml'
        writeXml(temp, img_name, width, height, ob, filename)
    os.rmdir(temp)