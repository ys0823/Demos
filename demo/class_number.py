'''
已有训练集数据的索引为train.txt
统计训练集中所有三种类别的ground truth 中bounding boxes 的数量
'''
#-*-coding:utf-8-*-
import re
import os
stcount = 0
sicount = 0
lycount = 0
#xml_foler = r'C:\Users\admin\Desktop\train.txt'
xml_foler = r'E:\yesheng data\project\data\VOC_2007_new_cleanout\ImageSets\Main\train.txt'
#xml_foler = r'E:\yesheng data\project\data\VCO_2007_div_poses\VCO_2007_div_poses\ImageSets\Main\val.txt'
name = []
name2 = []
with open(xml_foler) as f1:
    for line in f1:
        a = line.split('\n')
        name.append(a[0])
        if len(a[0])==6:
            name2.append(a[0])
print('picture num is: {}'.format(len(name2)))

# print(name)
# print(len(name))

# for j in range(len(f2)):
#   try:
#     with open("C:\\Users\\admin\\Desktop\\choose\\"+ name[j] + ".xml") as f:
#         s = f.read()
#         standing = re.findall("standing", s)
#         sitting = re.findall("sitting", s)
#         lying = re.findall('lying', s)
#         stcount = stcount + len(standing)
#         sicount = sicount + len(sitting)
#         lycount = lycount + len(lying)
#   except IOError:
#       continue
# print ("standing", stcount)
# print ("sitting", sicount)
# print ("lying", lycount)
number = 0
number2 =0

for j in range(len(name2)):
    with open("E:\\yesheng data\\project\\data\\VOC_2007_new_cleanout\\Annotations\\"+ name2[j] + ".xml") as f:
        s = f.read()
        standing = re.findall("standing", s)
        sitting = re.findall("sitting", s)
        lying = re.findall('lying', s)
        stcount = stcount + len(standing)
        sicount = sicount + len(sitting)
        lycount = lycount + len(lying)
        number += 1
print ("sitting", sicount)
print ("standing", stcount)
print ("lying", lycount)
#print("picture number",number)
stcount = 0
sicount = 0
lycount = 0
print('----------------------------------------------------------')
print('divide picture:\n')
print('divide_picture num is: {}'.format(len(name)))
for j in range(len(name)):
    with open("E:\\yesheng data\\project\\data\\VOC_2007_new_cleanout\\Annotations\\"+ name[j] + ".xml") as f:
        s = f.read()
        standing = re.findall("standing", s)
        sitting = re.findall("sitting", s)
        lying = re.findall('lying', s)
        stcount = stcount + len(standing)
        sicount = sicount + len(sitting)
        lycount = lycount + len(lying)
        number += 1

print ("sitting", sicount)
print ("standing", stcount)
print ("lying", lycount)
#print("picture number",number)

'''
for j in range(len(name)):
    with open("C:\\Users\\admin\\Desktop\\VOC_2007_part16\\VOC_2007_part16\\Annotations\\"+ name[j] + ".xml") as f:
        s = f.read()
        standing = re.findall("standing", s)
        sitting = re.findall("sitting", s)
        lying = re.findall('lying', s)
        stcount =len(standing)
        sicount =len (sitting)
        lycount = len(lying)
        if stcount ==0 and sicount ==0 and lycount == 0:
            number += 1
        number2 += 1
# print ("standing", stcount)
# print ("sitting", sicount)
# print ("lying", lycount)
print("background number",number)
print("total train number",number2)
'''

