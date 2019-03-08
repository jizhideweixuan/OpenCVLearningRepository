# -*- coding: utf-8 -*-
"""
霍夫变换
Probabilistic_Hough_Transform 是对霍夫变换的一种优化.
它不会对每一个点都进行计算,而是从一幅图像中随机选取
一个点集进行计算,对于直线检测来说这已经足够了.
但是使用这种变换我们必须要降低阈值（总的点数都少了,阈值肯定也要小）
cv2.HoughLinesP()
• minLineLength - 线的最短长度.比这个短的线都会被忽略.
• MaxLineGap - 两条线段之间的最大间隔,如果小于此值,这两条直线就被看成是一条直线
"""

import cv2
import numpy as np

# 读入
img = cv2.imread("./DataSource/sudoku.jpg")
# 转灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Canny边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10
# 霍夫
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
for x in lines:
    for x1, y1, x2, y2 in x:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 展示图片
cv2.imshow('res', img)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()

