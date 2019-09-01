import os
import shutil
from os import walk
'''
os.wallk真是个好接口
'''
num = 0 #file pair number
name = 7765
dir = 'E:\\yesheng data\\project\\data\\20190531 标注修正\\'
rename_dir = 'E:\\yesheng data\\project\\data\\20190531_change_name\\'
for parent, dirnames, filenames in os.walk(dir):
    #print(parent)
    #print(dirnames)
    #print(filenames)
    print('====================================================')
    if filenames != []:
        for i in range(len(filenames)):
            str_name1 = filenames[i].split('.')  #file name
            if str_name1[1] == 'jpg' or str_name1[1] == 'bmp' or str_name1[1] == 'png':
                for j in range(len(filenames)):
                    str_name2 = filenames[j].split('.')
                    if str_name1[0] == str_name2[0] and str_name1[1] == 'bmp' and str_name2[1] == 'xml' or \
                            str_name1[0] == str_name2[0] and str_name1[1] == 'jpg' and str_name2[1] == 'xml' or \
                            str_name1[0] == str_name2[0] and str_name1[1] == 'png' and str_name2[1] == '.xml':
                        oldname_pic = parent + '\\' + filenames[i]
                        newname_pic = rename_dir + '00'+ str(name) + '.jpg'
                        oldname_xml = parent + '\\' + filenames[j]
                        newname_xml = rename_dir +  '00'+ str(name) + '.xml'
                        shutil.copy(oldname_pic, newname_pic)
                        print(oldname_pic, '============>', newname_pic)
                        shutil.copy(oldname_xml, newname_xml)
                        print(oldname_xml, '============>', newname_xml)
                        num += 1
                        name += 1
print(num)



