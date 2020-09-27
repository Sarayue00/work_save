import cv2
import numpy as np

# 蓝换红 白换蓝
img = cv2.imread('D:/2.jpg')
dst = img.copy()
# 缩放
rows, cols, channels = dst.shape
dst = cv2.resize(dst, None, fx=0.5, fy=0.5)
rows, cols, channels = dst.shape
# 转换hsv
hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
# 点击获取hsv
# def getpos(event, x, y, flags, param):
#   if event == cv2.EVENT_LBUTTONDOWN:  # 定义一个鼠标左键按下去的事件
#     print(hsv[y, x])
# cv2.imshow("imageHSV",hsv)
# cv2.imshow('dst',dst)
# cv2.setMouseCallback("imageHSV", getpos)
# 设阈值
# lower_blue=np.array([90,70,70])
# upper_blue=np.array([110,255,255])
lower_white = np.array([0, 0, 245])  # 0 0 255 白色
upper_white = np.array([10, 10, 255])
mask = cv2.inRange(hsv, lower_white, upper_white)
# cv2.imshow('Mask', mask)

# 腐蚀膨胀
erode = cv2.erode(mask, None, iterations=1)
dilate = cv2.dilate(erode, None, iterations=1)

# 遍历替换
for i in range(rows):
  for j in range(cols):
    if dilate[i,j] == 255:
      dst[i, j] = (255, 0, 0)#此处替换颜色，为BGR通道

cv2.imwrite("D:/b.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()