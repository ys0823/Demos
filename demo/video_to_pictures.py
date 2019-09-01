import os.path
import cv2
def vide_read(filepath, savepath, frames):
    '''
    # windows版本，两层目录,可根据需要改进
    :param filepath: 视频所在大目录
    :param savepath: 图像保存目录
    :param frames: 帧读取速度
    :return: None
    '''
    pathDir = os.listdir(filepath)
    a = 0
    for allDir in pathDir:
        file_next = filepath + '\\' + allDir
        pathDir = os.listdir(file_next)
        for vide_next in pathDir:
            videpath_next = file_next + '\\' + vide_next
            print(videpath_next)
            vc = cv2.VideoCapture(videpath_next)
            c = 1
            if vc.isOpened():
                rval, frame = vc.read()
            else:
                rval = False

            while rval:
                rval, frame = vc.read()
                if (c % frames == 0):
                    cv2.imwrite(savepath + str(a) + '.jpg', frame)
                    a = a + 1
                c = c + 1
                cv2.waitKey(1)
            vc.release()
        print(a) #图片总数

