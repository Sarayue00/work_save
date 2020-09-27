import os.path

import os
base_path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_path, "norust\\JPEGImages")
print(data_dir)
#
# def generate_train_and_val(image_path, txt_file):
#     with open(txt_file, 'w') as tf:
#         for root, dirs, files in os.walk(image_path, topdown=False):
#             print("{}文件含{}张图片".format(txt_file, len(files)))
#             for file in files:
#                 tf.write(file.replace(".jpg", "") + '\n')

def generate_test_txt(image_path, txt_file):
    with open(txt_file, 'w') as f:
        for root, dirs, files in os.walk(image_path, topdown=False):
            for file in files:
                f.write('{}/{}' .format(image_path, file) + '\n')
#
#
# list_file = open('{}/screw_test.txt'.format(data_dir), 'w')
# list_file.write('{}/{}/JPEGImages/{}.jpg\n' .format(wd, data_dir, image_id))
generate_test_txt(data_dir, base_path + '/screw_test.txt')
# generate_train_and_val(test_path, path + '/test.txt')