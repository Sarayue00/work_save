import cv2
import os

base_file = "D:\\03-work\\03-data\\fangchenchui_2\\JPEGImages_chi_2"
img_file = os.path.join(base_file, "src_2")
rust_file = os.path.join(base_file, "rust\\JPEGImages")
norust_file = os.path.join(base_file, "norust\\JPEGImages")
delete_file = os.path.join(base_file, "delete")
img_dir = os.listdir(img_file)

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
makedir(img_file)    
makedir(rust_file)    
makedir(norust_file)   
makedir(delete_file)    
        
count = len(img_dir)
for i in range(len(img_dir)):
    img_path = os.path.join(img_file, img_dir[i])
    img_name = img_path.split("\\")[-1]
    img = cv2.imread(img_path)
    # cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
    cv2.imshow("image", img)
    k = cv2.waitKey(0) & 0xFF
    count -= 1
    if k == ord(' '):
        print("{}---->锈蚀，还剩{}".format(img_path, count))
        cv2.imwrite("{}/{}".format(rust_file, img_name), img)
    elif k == ord('d'):
        # os.remove(img_path)
        print("删除成功，还剩{}".format(count))
        cv2.imwrite("{}/{}".format(delete_file, img_name), img)
    elif k == ord('n'):
        print("{}---->正常，还剩{}".format(img_path, count))
        cv2.imwrite("{}/{}".format(norust_file, img_name), img)
    elif k == ord('q'):
        break

print("锈蚀的个数：{}".format(len(os.listdir(rust_file))))
print("正常的个数：{}".format(len(os.listdir(norust_file))))