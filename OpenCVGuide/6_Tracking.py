# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 图像跟踪

# 找到颜色的HSV值
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(green)

# 读入视频
cap = cv2.VideoCapture("./DataSource/vid.mp4")

while (1):
    # 读取每一帧
    _, frame = cap.read()
    # BGR颜色转HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设置黄色的HSV范围
    lower_yellow = np.array([11, 43, 46])
    upper_yellow = np.array([25, 255, 255])
    # 只取得黄色的图像色块,得到掩模
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # 对原图和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
