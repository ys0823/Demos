'''
将一张图片按[0.5,0.5]的比例均匀分为4块,并保存
'''
import cv2
import os
folder = "E:\\yesheng data\\learning\\python\\pytorch_learn\\pictures\\"
f = os.listdir(folder)
for i in range(len(f)-1):
    img = cv2.imread(folder+f[i])
    a = f[i].split('.')
    height = len(img)
    width = len(img[0])
    img_part1 = img[int(0):int(0.5*height),int(0):int(0.5*width)]
    img_part2 = img[int(0):int(0.5*height),int(0.5*width):int(width)]
    img_part3 = img[int(0.5*height):int(height),int(0):int(0.5*width)]
    img_part4 = img[int(0.5*height):int(height),int(0.5*width):int(width)]
    cv2.imwrite('E:\\yesheng data\\learning\\python\\pytorch_learn\\picture_dev\\'+a[0]+'_'+'part1.jpg',img_part1)
    cv2.imwrite('E:\\yesheng data\\learning\\python\\pytorch_learn\\picture_dev\\'+a[0]+'_'+'part2.jpg',img_part2)
    cv2.imwrite('E:\\yesheng data\\learning\\python\\pytorch_learn\\picture_dev\\'+a[0]+'_'+'part3.jpg',img_part3)
    cv2.imwrite('E:\\yesheng data\\learning\\python\\pytorch_learn\\picture_dev\\'+a[0]+'_'+'part4.jpg',img_part4)

