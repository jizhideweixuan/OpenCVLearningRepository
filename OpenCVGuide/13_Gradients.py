# -*- coding: utf-8 -*-
"""
图像梯度,即求一阶导数或二阶导数
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/1.jpg", 0)

# laplacian算子,拉普拉斯算子可以使用二阶导数的形式定义,可假设其离散实现类似于二阶 Sobel 导数
# CV_64F,深度
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# 参数:源,深度,(X方向一阶导,Y方向一阶导)最大二阶导,滤波模板(大于1的奇数)
# Sobel 算子是高斯平滑与微分操作的结合体,所以它的抗噪声能力很好。
# 你可以设定求导的方向(xorder 或 yorder).还可以设定使用的卷积核的大小(ksize).
# 如果 ksize=-1,会使用 3x3 的 Scharr 滤波器,它的的效果要比 3x3 的 Sobel 滤波器好(而且速度相同,
# 所以在使用 3x3 滤波器时应该尽量使用 Scharr 滤波器).
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

"""
可以使用参数-1设定输出图像深度和原图像一致,但是代码中使用了cv2.CV_64F

"""

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
