'''
用来更新每次的VOC2007训练集的train.txt,val.txt,trainval.txt
目的是找出原有的train.txt中的原图然后再新数据集上找到相应的原图以及原图被分块后的图片,保存在新的文件夹中
'''
import os
import shutil
train_txt_path = r'C:\Users\admin\Desktop\imagessets\train.txt'
ano_train_path = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_train'
ano_val_path = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations_val'
ano_path = r'C:\Users\admin\Desktop\VOC_2007_part16\VOC_2007_part16\Annotations'
num = 0
f2 = os.listdir(ano_path)
with open(train_txt_path) as f1:
    for line in f1:
        a = line.split('\n')
        if len(a[0]) == 6: #原图名字长度为6
            for i in range(len(f2)):
                b = f2[i].split('.')
                c = b[0][0:6] #取前6个字符跟原图字符比较
                if c==a[0]:
                    print(ano_path+f2[i])
                    shutil.copy(ano_path+'\\'+f2[i],ano_train_path+'\\'+f2[i]) #copy files from dir1 to dir2
                    num +=1
print(num)



