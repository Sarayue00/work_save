import os
import xml.etree.ElementTree as ET
import tqdm

import xml.dom.minidom



import os

import re

listdir = ['D:/03-work/03-data/rust_xianjia_1/rust/Annotations']

for i in listdir:

    for root, dirs, files in os.walk(i):

        for file in files:
            url = str(root) + str("/") + str(file)

            # print(url)

            # f = open(url, 'w',encoding= 'utf-8')  #"utf-8ansi"

            # text = f.read()
            # f.write(text.replace('\\','/'))
            # text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"/", text)
            infopen = open(url, 'r', encoding="utf-8")
            outfopen = open(url, 'w', encoding="utf-8")
            db = infopen.read(5)
            print(db)
            # outfopen.write(db.replace("xmin","123"))
            infopen.close()
            outfopen.close()
            # # f.close()
            # #
            # with open(url, "w", encoding="utf-8") as f1:
            #
            #     f1.write(db.replace('\\','/'))
