# -*- coding: utf-8 -*-
"""
Hough 圆环变换,霍夫梯度法
cv2.HoughCircles()
"""

import cv2
import numpy as np

img = cv2.imread("./DataSource/orange.jpg", 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# 参数:
# image :源,
# method :HOUGH_GRADIENT
# dp :累加器分辨率与图像分辨率的反比.例如,如果dp = 1,则累加器具有与输入图像相同的分辨率.
#       如果dp = 2,则累加器的宽度和高度都是一半.
# minDist :检测到的圆的中心之间的最小距离.如果参数太小,除了真实的一个之外,可能错误地检测到多个相邻的圆圈.
#           如果太大,可能会遗漏一些圈子.
# param1 :第一个特定于方法的参数.在HOUGH_GRADIENT的情况下,它是传递给Canny边缘检测器的两个较高的阈值（较低的一个是两倍小）
# param2 :第二种方法特定参数.在HOUGH_GRADIENT的情况下,它是检测阶段圆心的累加器阈值.它越小,可以检测到更多的假圆圈.将首先返回与较大累加器值对应的圆圈.
# minRadius :最小圆半径.
# maxRadius :最大圆半径.如果<= 0，则使用最大图像尺寸.如果<0，则返回中心而不查找半径.
circles = cv2.HoughCircles(img,  cv2.HOUGH_GRADIENT, 1, 400,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
