# https://blog.csdn.net/LOVE1055259415/article/details/79166754

import os.path
import xml.dom.minidom

path = "D:\\03-work\\03-data\\rust_xianjia_1\\rust\\Annotations"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开

        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
        root = dom.documentElement
        # 获取标签对name/pose之间的值
        name = root.getElementsByTagName('name')

        # 重命名class name
        for i in range(len(name)):
            name[i].firstChild.data = 'luoshuanxiushi'  # No corrosion of bolts


        # 保存修改到xml文件中
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('修改成功!')

