import os
from tqdm import tqdm
import cv2


# img
flag = 1
# flag = 0
if flag:
    base_path = "D:\\03-work\\03-data\\fangchenchui_2\\JPEGImages_chi_2"
    name_path = os.path.join(base_path, "src_2")
    rename_path = os.path.join(base_path, "rename")
    img_dir = os.listdir(name_path)

    def makedir(new_dir):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    makedir(rename_path)

    for i in tqdm(range(len(img_dir))):
        old_path = os.path.join(name_path, img_dir[i])
        new_path = os.path.join(rename_path, img_dir[i][:-4] + 'd.jpg')
        img = cv2.imread(old_path)
        # print(img_dir[i])
        cv2.imwrite(new_path, img)

# xml
# flag = 1
flag = 0
if flag:
    name_path = "D:/03-work/03-data/xianjia_rust_3/norust/name"
    rename_path = "D:/03-work/03-data/xianjia_rust_3/norust/rename"
    xml_dir = os.listdir(name_path)
    from xml.etree.ElementTree import ElementTree
    from os import walk, path
    import cv2
    import os


    def read_xml(in_path):
        tree = ElementTree()
        tree.parse(in_path)
        return tree


    def write_xml(tree, out_path):
        tree.write(out_path, encoding="utf-8", xml_declaration=True)


    def get_path_prex(rootdir):
        data_path = []
        prefixs = []
        for root, dirs, files in walk(rootdir, topdown=True):
            for name in files:
                pre, ending = path.splitext(name)
                if ending != ".xml":
                    continue
                else:
                    data_path.append(path.join(root, name))
                    prefixs.append(pre)

        return data_path, prefixs


    xml_paths, prefixs = get_path_prex(name_path)
    for i in range(len(xml_paths)):
        # rename and save the corresponding xml
        tree = read_xml(xml_paths[i])
        print(tree)
        # save output xml, 000001.xml
        write_xml(tree, "{}/{}{}.xml".format(rename_path, xml_dir[i][:-4], "a"))
