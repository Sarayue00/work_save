import os
from tqdm import tqdm
import cv2

# 锈蚀
# flag = 1
flag = 0
if flag:
    base_path = "D:\\03-work\\03-data\\fangchenchui_2\\JPEGImages_chi_2\\rust"
    img_file = os.path.join(base_path, "JPEGImages")
    txt_file = os.path.join(base_path, "label")
    img_dir = os.listdir(img_file)

    def makedir(new_dir):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
    # makedir(img_file)
    makedir(txt_file)

    for i in tqdm(range(len(img_dir))):
        img_path = os.path.join(img_file, img_dir[i])
        txt_path = os.path.join(txt_file, img_dir[i][:-4] + ".txt")
        img = cv2.imread(img_path)
        h, w = img.shape[:-1]
        X = 1/2 - 1/w
        Y = 1/2 - 1/h
        W = 1/7   # 1/3
        H = 1/3
        with open(txt_path, 'w') as f:
            f.write("{} {} {} {} {}".format(0, X, Y, W, H))


# 不锈
flag = 1
# flag = 0
if flag:
    base_path = "D:\\03-work\\03-data\\fangchenchui_2\\JPEGImages_C\\norust"
    img_file = os.path.join(base_path, "JPEGImages")
    txt_file = os.path.join(base_path, "label")
    img_dir = os.listdir(img_file)

    def makedir(new_dir):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

    # makedir(img_file)
    makedir(txt_file)

    for i in tqdm(range(len(img_dir))):
        img_path = os.path.join(img_file, img_dir[i])
        txt_path = os.path.join(txt_file, img_dir[i][:-4] + ".txt")
        with open(txt_path, 'w') as f:
            f.write("")
