import os
import xml.etree.ElementTree as ET
import tqdm


def del_delete_eq_1(xml_path):
    # 从xml文件中读取，使用getroot()获取根节点，得到的是一个Element对象

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for object in root.findall('object'):

        name = str(object.find('name').text)
        # n = 0
        if (name in ["luoshuan"]):
            root.remove(object)
            # n = 1
        else:
            pass


    tree.write(xml_path)
    # return n


def main():
    root_dir = "D:/03-work/03-data/xianjia_rust_2/norust/Annotations"
    xml_path_list = [os.path.join(root_dir, x) for x in os.listdir(root_dir)]
    # count = 0
    for xml in tqdm.tqdm(xml_path_list):
        print(xml)
        # m = del_delete_eq_1(xml)
        del_delete_eq_1(xml)
        # count += m
    # print(count)


if __name__ == '__main__':
    main()

