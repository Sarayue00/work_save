import cv2
img_1 = cv2.imread("D:/chart_yolov4_.png")
img_2 = cv2.imread("D:/chart_yolov4_1.png")
add_img = cv2.addWeighted(img_1, 0.6, img_2, 0.4, 0)  # 图像融合
cv2.imshow("add_img", add_img)
cv2.waitKey(0)
cv2.imwrite("D:/add_img.png", add_img)