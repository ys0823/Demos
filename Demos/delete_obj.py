import os
import xml.etree.ElementTree as ET

xml_path = 'C:\\Users\\admin\\Desktop\\test\\00020.xml'
train_ano = r'C:\Users\admin\Desktop\test_ano'
xml_list = os.listdir(train_ano)
number = 0
for xml_pa in xml_list:
    #print(xml_path)
    xml_path = train_ano + '\\' +xml_pa
    tree = ET.parse(xml_path)
    root = tree.getroot()
    owner = root.find('owner')
    if owner is not None:
        root.remove(owner)
        tree.write(xml_path)
        print(xml_pa)
        number += 1
print(number)


