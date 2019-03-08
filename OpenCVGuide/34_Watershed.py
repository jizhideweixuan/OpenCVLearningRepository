# -*- coding: utf-8 -*-
"""
分水岭图像切割算法
cv2.HoughCircles()
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/coins.jpg")
# 灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Otsu's 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 显示图片
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 去除噪音
# 当硬币没有接触时,使用腐蚀操作可以有效的去除边缘像素.
# 当硬币互相接触时,更好的操作是距离变换再加上适合的阈值,再进行膨胀操作

# 设置核
kernel = np.ones((3, 3), np.uint8)
# 开运算,先腐蚀后膨胀
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 膨胀操作,将对象边界延伸到背景中
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 显示图片
cv2.imshow('sure_bg', sure_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Finding sure foreground area
# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离,也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现,腐蚀操作的停止条件是所有前景像素都被完全腐蚀.
# 这样根据腐蚀的先后顺序,我们就得到各个前景像素点到前景中心呗Ⅵ像素点的距离.
# 根据各个像素点的距离值,设置为不同的灰度值.这样就完成了二值图像的距离变换
# cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C

# 调整距离
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 二值化,得到确定区域
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# 显示图片
cv2.imshow('sure_fg', sure_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 得到未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 显示图片
cv2.imshow('unknown', unknown)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 生成标记
ret, markers = cv2.connectedComponents(sure_fg)

# 将确定区域标记为正整数
markers = markers + 1

# 将未知区域标记为0
markers[unknown == 255] = 0

# 使用分水岭算法
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
# 显示图片
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


