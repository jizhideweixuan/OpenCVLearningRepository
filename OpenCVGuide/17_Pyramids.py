# -*- coding: utf-8 -*-
"""
利用图像金字塔融合
有两类图像金字塔:高斯金字塔和拉普拉斯金字塔.
高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的.
顶部图像中的每个像素值等于下一层图像中 5 个像素的高斯加权平均值.
这样操作一次一个 MxN 的图像就变成了一个 M/2xN/2 的图像.
所以这幅图像的面积就变为原来图像面积的四分之一.这被称为 Octave.
连续进行这样的操作我们就会得到一个分辨率不断下降的图像金字塔.
我们可以使用函数cv2.pyrDown() 和 cv2.pyrUp() 构建图像金字塔。
函数 cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔（尺寸变小，分辨率降低）.反之
"""
import cv2
import numpy as np, sys

A = cv2.imread("./DataSource/apple.jpg")
B = cv2.imread("./DataSource/orange.jpg")

# 确认A,B分辨率相同
print(A.shape, B.shape)

# 生成A的高斯金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    # 高分辨率大尺寸向上构建金字塔
    G = cv2.pyrDown(G)
    gpA.append(G)

# 生成B的高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# 生成A的拉普拉斯金字塔
#
lpA = [gpA[5]]
for i in range(6, 0, -1):
    # 低分辨率向下构建金字塔
    GE = cv2.pyrUp(gpA[i])
    GE = cv2.resize(GE, gpA[i - 1].shape[-2::-1])
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)

# 生成B的拉普拉斯金字塔
lpB = [gpB[5]]
for i in range(6, 0, -1):
    # 向上构建金字塔
    GE = cv2.pyrUp(gpB[i])
    GE = cv2.resize(GE, gpB[i - 1].shape[-2::-1])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# 在金字塔的每一层,左右两边的图像融合
LS = []
lpAc = []
for i in range(len(lpA)):
    b = cv2.resize(lpA[i], lpB[i].shape[-2::-1])
    lpAc.append(b)
j = 0
for i in zip(lpAc, lpB):
    la, lb = i
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
    j = j + 1
    LS.append(ls)

# 根据融合后的金字塔重建图像,ls_结果是拉普拉斯拼接
# LS[0]是高斯金字塔最小的图片
ls_ = LS[0]
# 第一次循环为高斯金字塔的最小图片,一次通过拉普拉斯金字塔恢复到最大
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.resize(ls_, LS[i].shape[-2::-1])
    ls_ = cv2.add(ls_, LS[i])

# real结果是把两半直接拼接
B = cv2.resize(B, A.shape[-2::-1])
real = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))

cv2.imshow('ls_', ls_)
cv2.imshow('real', real)

# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
