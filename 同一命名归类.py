import os.path


# flag = 1
flag = 0
if flag:

    # 以jpg为目标删除xml  最终两者文件一样
    jpg_path = "D:/03-work/03-data/small_jueyuanzi/JPEGImages"
    xml_path = "D:/03-work/03-data/small_jueyuanzi/Annotations"
    # jpg_path = "D:/03-work/03-data/screw_5/rust"
    # xml_path = "D:/03-work/03-data/screw_5/Annotations"
    jpg_file = []
    for root, dirs, files in os.walk(jpg_path, topdown=False):
        for file in files:
            jpg_file.append(file.replace(".jpg",".xml"))
    print(jpg_file)

    for root, dirs, files in os.walk(xml_path, topdown=False):
        for file in files:
            print(file)
            if file not in jpg_file:
                os.remove(xml_path + "/" + file)

# flag = 1
flag = 0
if flag :
    # 以xml为目标删除jpg
    # jpg_path = "D:/03-work/03-data/big_picture/rust/JPEGImages"
    # xml_path = "D:/03-work/03-data/big_picture/rust/Annotations"
    jpg_path = "D:/03-work/03-data/xianjia_rust_3/norust/JPEGImages"
    xml_path = "D:/03-work/03-data/xianjia_rust_3/norust/Annotations"
    xml_file = []
    for root, dirs, files in os.walk(xml_path, topdown=False):
        for file in files:
            xml_file.append(file.replace(".xml", ".jpg"))
    print(xml_file)

    for root, dirs, files in os.walk(jpg_path, topdown=False):
        for file in files:
            print(file)
            if file not in xml_file:
                os.remove(jpg_path + "/" + file)


flag = 1
# flag = 0
if flag:
    # 以jpg为目标删除jpg  删除重复的，最终两者互补
    src_path = "D:\\03-work\\03-data\\fangzhenchui_1\\JPEGImages_1\\src"
    dst_path = "D:\\03-work\\03-data\\fangzhenchui_1\\JPEGImages_2\\src"

    src_file = []
    for root, dirs, files in os.walk(src_path, topdown=False):
        for file in files:
            src_file.append(file)
    print(src_file)

    for root, dirs, files in os.walk(dst_path, topdown=False):
        for file in files:
            print(file)
            if file in src_file:
                os.remove(dst_path + "/" + file)