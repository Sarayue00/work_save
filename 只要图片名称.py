import glob
import os.path

path = 'D:/03-work/03-data/rust_xianjia_6/split_text'
train_path = os.path.join(path, "train")
test_path = os.path.join(path, "test")


def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for root, dirs, files in os.walk(image_path, topdown=False):
            print("{}文件含{}张图片".format(txt_file, len(files)))
            for file in files:
                print(file)

                tf.write(file[:-4] + '\n')


generate_train_and_val(train_path, path + '/train.txt')
generate_train_and_val(test_path, path + '/test.txt')
