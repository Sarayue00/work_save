import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = [('screw', 'train'),('screw', 'test')]
classes = ['luoshuanxiushi']
data_dir = '08-rust_xianjia_4'


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(name, image_id):
    in_file = open('{}/Annotations/{}.xml'.format(data_dir, image_id),'rb')
    out_file = open('{}/labels/{}.txt' .format(data_dir, image_id), 'w')
    print('Annotations/%s.xml' % (image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

for name, image_set in sets:
    if not os.path.exists('{}/labels/'.format(data_dir)):
        os.makedirs('{}/labels/'.format(data_dir))

    
    image_ids = open('{}/ImageSets/Main/{}.txt'.format(data_dir, image_set)).read().strip().split()
    list_file = open('{}/{}_{}.txt'.format(data_dir, name, image_set), 'w')
    for image_id in image_ids:
        list_file.write('{}/{}/JPEGImages/{}.jpg\n' .format(wd, data_dir, image_id))
        convert_annotation(name, image_id)
    list_file.close()