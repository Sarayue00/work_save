# 切割图片    按名称切割放入文件夹
import xml.etree.ElementTree as ET
import cv2
import os
from lxml import etree
from tqdm import tqdm
class GEN_Annotations:
    def __init__(self, filename):
        self.root = etree.Element("annotation")

        child1 = etree.SubElement(self.root, "folder")
        child1.text = "VOC2007"

        child2 = etree.SubElement(self.root, "filename")
        child2.text = filename

        child3 = etree.SubElement(self.root, "source")

        child4 = etree.SubElement(child3, "annotation")
        child4.text = "PASCAL VOC2007"
        child5 = etree.SubElement(child3, "database")
        child5.text = "Unknown"

        child6 = etree.SubElement(child3, "image")
        child6.text = "flickr"
        child7 = etree.SubElement(child3, "flickrid")
        child7.text = "35435"

    def set_size(self, witdh, height, channel):
        size = etree.SubElement(self.root, "size")
        widthn = etree.SubElement(size, "width")
        widthn.text = str(witdh)
        heightn = etree.SubElement(size, "height")
        heightn.text = str(height)
        channeln = etree.SubElement(size, "depth")
        channeln.text = str(channel)

    def savefile(self, filename):
        tree = etree.ElementTree(self.root)
        tree.write(filename, pretty_print=True, xml_declaration=False, encoding='utf-8')

    def add_pic_attr(self, label, xmin, ymin, xmax, ymax):
        object = etree.SubElement(self.root, "object")
        namen = etree.SubElement(object, "name")
        namen.text = label
        bndbox = etree.SubElement(object, "bndbox")
        xminn = etree.SubElement(bndbox, "xmin")
        xminn.text = str(xmin)
        yminn = etree.SubElement(bndbox, "ymin")
        yminn.text = str(ymin)
        xmaxn = etree.SubElement(bndbox, "xmax")
        xmaxn.text = str(xmax)
        ymaxn = etree.SubElement(bndbox, "ymax")
        ymaxn.text = str(ymax)

def get_ext(w,h,b):
    # up down 100 left right 50
    b1 = []
    # print(b[0],b[1],b[2],b[3])
    b1.append(max(0, b[0] - 5))
    b1.append(max(0, b[1] - 5))
    b1.append(min(w, b[2] + 5))
    b1.append(min(h, b[3] + 5))
    return b1
# 原图
path_img = 'D:\\03-work\\03-data\\src\\JPEGImages\\'
path_xml = 'D:\\03-work\\03-data\\src\\Annotations\\'
# 切割后
out_path_img = 'D:\\03-work\\03-data\\dst\\JPEGImages\\'
out_path_xml = 'D:\\03-work\\03-data\\dst\\Annotations\\'

def makedir(*new_dir):
    for dir in new_dir:
        if not os.path.exists(dir):
            os.makedirs(dir)


makedir(out_path_img, out_path_xml)


img_dir = os.listdir(path_img)
xml_dir = os.listdir(path_xml)
idx = 0

#clss = ['jueyuanzi','junyahuan','zhishipai','bileiqi','hengdan','tonggan','fangzhenchui','baogu']#niaochao,xianjia
clss = ['zhishipai']

for i in tqdm(range(len(img_dir))):
    xml_path = os.path.join(path_xml, img_dir[i][:-3]+'xml')
    jpg_file = os.path.join(path_img, img_dir[i])
    if not os.path.exists(xml_path):
        continue
    im = cv2.imread(jpg_file)
    tree = ET.parse(xml_path)  # 解析xml
    root = tree.getroot()
    size = root.find('size')  # 图片尺寸<Element 'size' at 0x000002A6DF8DB778>

    w = int(size.find('width').text)  # 图片的宽
    # print(w)
    h = int(size.find('height').text)  # 图片的高
    is_show = False
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls in clss:
            is_show = True
            xmlbox = obj.find('bndbox')
            b = [float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymax').text)]
            b1 = get_ext(w, h, b)
            xmin, ymin, xmax, ymax = int(b[0] - b1[0]), int(b[1] - b1[1]), int(b[2] - b1[0]), int(b[3] - b1[1])
            new_img = im[int(b1[1]):int(b1[3]), int(b1[0]):int(b1[2])].copy()
            idx += 1
            new_img_path = os.path.join(out_path_img, img_dir[i][:-4]+'_'+str(idx).zfill(6)+".jpg")
            new_xml_path = os.path.join(out_path_xml, img_dir[i][:-4]+'_'+str(idx).zfill(6)+".xml")
            # 写图片
            # print('图片',new_img_path)
            cv2.imwrite(new_img_path,new_img)
            # 写标签
            anno = GEN_Annotations(new_img_path)
            nh, nw, nc = new_img.shape
            anno.set_size(nw, nh, nc)
            anno.add_pic_attr(cls, xmin, ymin, xmax, ymax)
            # print('xml', new_xml_path)
            anno.savefile(new_xml_path)
            cv2.waitKey(0)