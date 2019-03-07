# -*- coding: utf-8 -*-
"""
查找轮廓的不同特征,例如面积,周长,重心,d 边界框等
"""
import cv2
import numpy as np

img = cv2.imread("./DataSource/1.jpg", 0)

# 全局阈值
ret, thresh = cv2.threshold(img, 127, 255, 0)

# 找轮廓
contours, hierarchy = cv2.findContours(thresh, 1, 2)

# 得到矩
cnt = contours[0]
M = cv2.moments(cnt)
print("矩", M)

# 计算重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print("CX: ", cx, "CY: ", cy)

# 计算面积
area = cv2.contourArea(cnt)
print("面积: ", area)

# 轮廓周长
perimeter = cv2.arcLength(cnt, True)
print("周长: ", perimeter)

# 轮廓近似
#     将轮廓形状近似到另外一种由更少点组成的轮廓形状,新轮廓的点的数目
# 由我们设定的准确度来决定.使用的Douglas-Peucker算法,你可以到维基百
# 科获得更多此算法的细节.
#     为了帮助理解,假设我们要在一幅图像中查找一个矩形,但是由于图像的
# 种种原因,我们不能得到一个完美的矩形,而是一个"坏形状".
# 现在你就可以使用这个函数来近似这个形状（）了.这个函数的第二个参数叫
# epsilon,它是从原始轮廓到近似轮廓的最大距离.它是一个准确度参数.选
# 择一个好的 epsilon 对于得到满意结果非常重要.
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
print("approx: ", approx)

#   凸包与轮廓近似相似,但不同,虽然有些情况下它们给出的结果是一样的.
# 函数 cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷,并能纠
# 正缺陷.一般来说,凸性曲线总是凸出来的,至少是平的.如果有地方凹进去
# 了就被叫做凸性缺陷.例如下图中的手.红色曲线显示了手的凸包,凸性缺陷
# 被双箭头标出来了.
hull = cv2.convexHull(cnt)
print("hull: ", hull)

# 凸性检测,检测是不是凸的
k = cv2.isContourConvex(cnt)
print("k_hull: ", k)

