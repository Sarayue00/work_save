import os.path

import os
base_path = os.path.abspath(__file__)
data_dir = os.path.join(base_path,"09-test_xianjia")

#
# def generate_train_and_val(image_path, txt_file):
#     with open(txt_file, 'w') as tf:
#         for root, dirs, files in os.walk(image_path, topdown=False):
#             print("{}文件含{}张图片".format(txt_file, len(files)))
#             for file in files:
#                 tf.write(file.replace(".jpg", "") + '\n')

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for root, dirs, files in os.walk(image_path, topdown=False):
            print("{}文件含{}张图片".format(txt_file, len(files)))
            for file in files:
                print(file)

                tf.write(file[:-4] + '\n')
list_file = open('{}/screw_test.txt'.format(data_dir), 'w')
list_file.write('{}/{}/JPEGImages/{}.jpg\n' .format(wd, data_dir, image_id))
generate_train_and_val(train_path, path + '/train.txt')
generate_train_and_val(test_path, path + '/test.txt')