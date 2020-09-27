
import os.path
flag = 1
# flag = 0
if flag :
    # jpg_path = "D:\\03-work\\03-data\\xianjia_rust_2\\xianjia_rust_2\\JPEGImages"
    # jpg_path = "D:\\03-work\\03-data\\xianjia_rust_2\\xianjia_rust_2\\Annotations"
    jpg_path = "D:/03-work/03-data/fangchenchui_2/JPEGImages_chi_2/src_2"
    for root, dirs, files in os.walk(jpg_path, topdown=False):
        for file in files:
            # file.replace('.xml',)
            if file.find(" ") != -1:
                print(file)
                os.rename(jpg_path+'//'+file, jpg_path+'//'+file.replace(" ",""))


# flag = 1
flag = 0
if flag:
    jpg_path = "D:\\03-work\\03-data\\rust_xianjia_4\\split_text\\test"

    for root, dirs, files in os.walk(jpg_path, topdown=False):
        for file in files:
            # file.replace('.xml',)
            if file.find(" ") != -1:
                os.rename(jpg_path + '//' + file, jpg_path + '//' + file.replace(" ", ""))
