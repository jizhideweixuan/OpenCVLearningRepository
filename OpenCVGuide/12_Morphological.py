# -*- coding: utf-8 -*-
"""
图像形态
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/1.jpg", 0)
# 使用5x5的卷积核
kernel = np.ones((5, 5), np.uint8)
# 腐蚀,这个操作会把前景物体的边界腐蚀掉
# 如果与卷积核对应的原图像的所有像素值都是 1,那么中心元素就保持原来的像素值，否则就变为零
erosion = cv2.erode(img, kernel, iterations=1)
# 膨胀,与卷积核对应的原图像的像素值中只要有一个是 1,中心元素的像素值就是 1.所以这个操作会增加图像中的白色区域（前景）
dilation = cv2.dilate(img, kernel, iterations=1)
# 先进性腐蚀再进行膨胀就叫做开运算,它被用来去除噪声.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 先膨胀再腐蚀.它经常被用来填充前景物体中的小洞,或者前景物体上的小黑点.
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 形态学梯度,图像膨胀与腐蚀的差
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# 礼帽,原始图像与进行开运算之后得到的图像的差
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# 黑帽,进行闭运算之后得到的图像与原始图像的差。
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

images = [img, img, erosion,
          dilation, opening, closing,
          gradient, tophat, blackhat]
titles = ['Original', 'Original', 'Erosion',
          'dilation', 'opening', "closing",
          'gradient', 'tophat', "blackhat"]

for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
