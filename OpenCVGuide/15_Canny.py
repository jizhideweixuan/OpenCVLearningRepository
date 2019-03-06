# -*- coding: utf-8 -*-
"""
Canny边缘检测
原理:高斯滤波->Sobel算子计算水平和竖直方向的一阶导数->
    非极大值抑制(去掉非极大值的梯度点)->
    滞后阈值(确定min,max 当灰度梯度高于max确认为真的边界,低于min则抛弃,两者之间看是否与真边界相连,是则认为是真边界)
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/1.jpg", 0)
# 参数: 源,minVal,maxVal,Sobel核大小(默认3),L2gradient(Tru则使用L2梯度方程,False则使用Edge−Gradient,默认为False)
edges = cv2.Canny(img, 100, 200)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
