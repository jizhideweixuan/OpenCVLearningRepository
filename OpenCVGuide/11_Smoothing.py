# -*- coding: utf-8 -*-
"""
图像模糊(去噪)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/1.jpg", cv2.IMREAD_COLOR)

# 这是一个5x5的平均滤波器核
# 5*5个像素取平均值
avg = blur = cv2.blur(img, (5, 5))

# 高斯模糊,详见10_
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 中值模糊,详见9_
median = cv2.medianBlur(img, 5)

# 双边滤波,能在保持边界清晰的情况下有效的去除噪音,但是这种操作与其他滤波器相比会比较慢.
# 在使用高斯滤波的同时考虑其边界
# 参数:源,邻域直径,空间高斯函数标准差,灰度值相似性高斯函数标准差
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['Original Image', 'Original Image', 'avg', 'gaussian', 'median', 'bilateral']
images = [img, img, avg, gaussian, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

