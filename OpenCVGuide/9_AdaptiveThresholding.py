# -*- coding: utf-8 -*-
import cv2
from matplotlib import pyplot as plt

# 自适应阈值

img = cv2.imread("./DataSource/1.jpg",0)
# 中值滤波,是基于排序统计理论的一种能够有效抑制噪声的非线性信号处理技术,
# 基本思想是用像素点邻域灰度值的中值来代替该像素点的灰度值,让周围的像素值接近真实的值从而消除孤立的噪声点.
# 该方法在取出脉冲噪声,椒盐噪声的同时能保留图像的边缘细节.这些优良特性是线性滤波所不具备的.
# medianBlur(InputArray src,int ksize) ksize 滤波模板,必须是大于1的奇数
img = cv2.medianBlur(img, 5)

# 全局阈值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 参数:源,maxlevel,AdaptiveMethod,BlockSize,C,
# Adaptive Method - 指定计算阈值的方法.
# cv2.ADPTIVE_THRESH_MEAN_C :阈值取自相邻区域的平均值.
# cv2.ADPTIVE_THRESH_GAUSSIAN_C :阈值取值相邻区域的加权和,权重为一个高斯窗口.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
