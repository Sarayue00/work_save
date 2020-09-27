import os
import random
import shutil

# 二分类
BASE_DIR = 'D:/03-work/03-data/rust_xianjia_6/'

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


if __name__ == '__main__':

    dataset_dir = os.path.abspath(os.path.join(BASE_DIR, "split_data"))
    split_dir = os.path.abspath(os.path.join(BASE_DIR, 'split'))
    train_dir = os.path.join(split_dir, "train")
    test_dir = os.path.join(split_dir, "test")

    train_pct = 0.93
    test_pct = 0.06

    for root, dirs, files in os.walk(dataset_dir):
        print(dirs)
        for sub_dir in dirs:

            imgs = os.listdir(os.path.join(root, sub_dir))
            imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
            random.shuffle(imgs)
            img_count = len(imgs)

            train_point = int(img_count * train_pct)
            test_point = int(img_count * (train_pct + test_pct))

            for i in range(img_count):
                if i < train_point:
                    out_dir = os.path.join(train_dir, sub_dir)
                else:
                    out_dir = os.path.join(test_dir, sub_dir)
                makedir(out_dir)

                target_path = os.path.join(out_dir, imgs[i])
                src_path = os.path.join(dataset_dir, sub_dir, imgs[i])

                shutil.copy(src_path, target_path)

            print('Class:{}, train:{}, test:{}'.format(sub_dir, train_point, test_point-train_point,))
            print("已在 {} 创建划分好的数据\n".format(out_dir))