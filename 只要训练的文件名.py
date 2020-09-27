import glob
import os.path
import random
import shutil
# 生成train.txt
train_path = 'D:/03-work/03-data/xianjia_rust_3/train'
txt_file = 'D:/03-work/03-data/xianjia_rust_3/train.txt'
imgs = os.listdir(train_path)
imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
random.shuffle(imgs)


with open(txt_file, 'w') as tf:

    for img in imgs:
        # tf.write(img.replace(".jpg", "") + '\n')
        tf.write(img[:-4] + '\n')

print(tf)

