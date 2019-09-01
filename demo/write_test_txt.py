import os
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

save_path = 'E:\\yesheng data\\project\\head count\\VOCdevkit\\VOC2007\\annotations_txt'
test_xml = r'E:\yesheng data\project\head count\VOCdevkit\coco\test_ano_4part'
test_list = os.listdir(test_xml)

#print(test_list)
number = 0
for test in test_list:
    if len(test.split('.')[0]) == 5:
        with open(save_path + '\\' + test.split('.')[0] + '.txt', 'w+') as f:

            path = os.path.join(test_xml, test)
            tree = ET.ElementTree(file=path)
            root = tree.getroot()
            box = []
            for label in root.findall('object'):
                x1 = (int(float(label[4][0].text)))
                y1 = (int(float(label[4][1].text)))
                x2 = (int(float(label[4][2].text)))
                y2 = (int(float(label[4][3].text)))
                bndx = str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + '\n'
                f.write(bndx)
        number += 1

print(number)



