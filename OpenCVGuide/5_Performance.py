# -*- coding: utf-8 -*-
import cv2

# 性能表现

# 执行时长
img1 = cv2.imread("./DataSource/1.jpg", 0)
# 获取当前时钟getTickCount()
e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
# getTickFrequency()获取时钟频率,t是程序执行的时长
t = (e2 - e1) / cv2.getTickFrequency()
print(t)
