# -*- coding: utf-8 -*-
"""
简单阈值(全局阈值)
"""
import cv2
from matplotlib import pyplot as plt

# 原图像应该是灰度图
img = cv2.imread("./DataSource/1.jpg", 0)
# double threshold(InputArray src,double thresh, double maxval, int type)
# 参数: 源,目标,分类阈值,当高于阈值时赋的值,阈值方法
# THRESH_BINARY 当前点值大于阈值时，取Maxval,也就是第三个参数，下面再不说明，否则设置为0
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# THRESH_BINARY_INV 当前点值大于阈值时，设置为0，否则设置为Maxval
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# THRESH_TRUNC 当前点值大于阈值时，设置为阈值，否则不改变
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# THRESH_TOZERO 当前点值大于阈值时，不改变，否则设置为0
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#   THRESH_TOZERO_INV  当前点值大于阈值时，设置为0，否则不改变
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
