# -*- coding: utf-8 -*-
"""
霍夫变换
cv2.HoughLines()
这个函数的第一个参数是一个二值化图像,
所以在进行霍夫变换之前要首先进行二值化,或者进行Canny 边缘检测
第二和第三个值分别代表 ρ 和 θ 的精确度.
第四个参数是阈值,只有累加其中的值高于阈值时才被认为是一条直线,
也可以把它看成能检测到的直线的最短长度（以像素点为单位）
"""

import cv2
import numpy as np

# 读入
img = cv2.imread("./DataSource/sudoku.jpg")
# 转灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Canny边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# 霍夫变换
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for x in lines:
    for rho, theta in x:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 展示图片
cv2.imshow('res', img)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()

