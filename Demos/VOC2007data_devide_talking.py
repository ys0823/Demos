import os
import random
import xml.etree.cElementTree as ET
import shutil
'''
total data is 726 pictures
test: 182 pictures
trainval: 544 pictures
train: 272 pictures
'''

#删除talking外的标签
path_root = ['E:/yesheng data/project/data/VOC_2007_talking_new/VOC2007_Include_Talking/Annotations']
# CLASSES = [
#     "sitting","standing", "lying",'groveling']
CLASSES = ['sitting','lying','standing'] #要删掉的类别
n = 0
talking_pic = []
#删除除talking外的标签
for anno_path in path_root:
    xml_list = os.listdir(anno_path)
    for axml in xml_list:
        path_xml = os.path.join(anno_path, axml)
        tree = ET.parse(path_xml)
        root = tree.getroot()
        for child in root.findall('object'):
            name = child.find('name').text
                #if name == 'groveling':
                #child.find('name').text = 'lying'
            for na in CLASSES:
                if name == na:
                    root.remove(child)
        for child in root.findall('object'):
            name = child.find('name').text
            if name == 'talking':
                tree.write(os.path.join(r'E:/yesheng data/project/data/VOC_2007_talking_new/Annotations', axml))  #修改后xml文件的存储路径
        print(axml)

#trainval_percent = 1# trainval数据集占所有数据的比例
train_percent = 0.5# train数据集占trainval数据的比例
xmlfilepath = 'E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\Annotations'
jpegfilepath = r'E:\yesheng data\project\data\VOC2007_Include_Talking\JPEGImages'
jpegsavepath = r'E:\yesheng data\project\data\VOC_2007_talking_new\jpeg'
txtsavepath = 'E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\ImageSets\\Main'
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list=range(num)

trainval = []
test = [] #test id
for i in range(num):
    if i % 6 ==0:
        test.append(i)
    else:
        trainval.append(i)
train_ratio = int(len(trainval)*train_percent)
train = random.sample(trainval,train_ratio)
val = [i for i in trainval if i not in train]
trainval_id = train.copy()
trainval_id.extend(val)

ftrainval = open('E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\ImageSets\\Main\\trainval.txt', 'w')
ftest = open('E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\ImageSets\\Main\\test.txt', 'w')
ftrain = open('E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\ImageSets\\Main\\train.txt', 'w')
fval = open('E:\\yesheng data\\project\\data\\VOC_2007_talking_new\\ImageSets\\Main\\val.txt', 'w')
n = 0

trainval_list = []
for i in list:
    name = total_xml[i][:-4] + '\n'
    # if i in trainval:
    #     ftrainval.write(name)
    if i in train:
        ftrain.write(name)
    elif i in val:
        fval.write(name)
    else:
        ftest.write(name)
    n +=1
print(n)
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()

'''
用于处理jpeg数据
'''
trainval_txt = r'E:\yesheng data\project\data\VOC_2007_talking_new\ImageSets\Main\trainval.txt'
test_txt = r'E:\yesheng data\project\data\VOC_2007_talking_new\ImageSets\Main\test.txt'
n = 0
with open(trainval_txt,'r') as f1:
    for line in f1:
        line = line.split('\n')
        try:
            shutil.copy(jpegfilepath + '\\'+ line[0] + '.jpg',jpegsavepath + '\\' +line[0] + '.jpg')
            print(jpegfilepath +'\\' + line[0] + '.jpg','=========>',jpegsavepath +'\\'+  line[0] + '.jpg')
            n+=1
        except FileNotFoundError:
            continue

with open(test_txt,'r') as f2:
    for line in f2:
        line = line.split('\n')
        try:
            shutil.copy(jpegfilepath + '\\'+ line[0] + '.jpg',jpegsavepath + '\\' +line[0] + '.jpg')
            print(jpegfilepath +'\\' + line[0] + '.jpg','=========>',jpegsavepath +'\\'+  line[0] + '.jpg')
            n +=1
        except FileNotFoundError:
            continue
print(n)

