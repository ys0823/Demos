'''
已有训练集数据的索引为train.txt
统计训练集中所有三种类别的ground truth 中bounding boxes 的数量
'''
#-*-coding:utf-8-*-
import re
import os
import shutil

#folder
train_txt_folder = r'C:\Users\admin\Desktop\ImageSets\Main\train.txt'
val_txt_folder = r'C:\Users\admin\Desktop\ImageSets\Main\val.txt'

#xml_train_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_train'
#xml_val_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_val'
xml_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations'
#picture path
pic_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\JPEGImages'
pic_train_save_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\train_choose'
pic_val_save_folder =r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\val_choose'

#xml save path
xml_train_save_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_train_nonback'
xml_val_save_folder = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_val_nonback'


train_name = []
val_name = []

#train.txt
with open(train_txt_folder) as f1:
    for line in f1:
        a = line.split('\n')
        train_name.append(a[0])

#val.txt
with open(val_txt_folder) as f2:
    for line in f2:
        b = line.split('\n')
        val_name.append(b[0])
number = 0 #total non back number
number2 =0

for j in range(len(val_name)):
    with open(xml_folder + '\\'+ val_name[j] + ".xml") as f:
        s = f.read()
        totalcount = 0
        standing = re.findall("standing", s)
        sitting = re.findall("sitting", s)
        lying = re.findall('lying', s)

        stcount =len(standing)
        sicount =len (sitting)
        lycount = len(lying)
        totalcount = stcount + sicount + lycount
        if totalcount != 0:
            number += 1
            shutil.copy( xml_folder+ '\\' + val_name[j]+'.xml', xml_val_save_folder  + '\\' + val_name[j]+'.xml')
            print('deal with {}'.format(xml_val_save_folder + val_name[j] +'.xml'))

print('total non back number is {}'.format(number))




