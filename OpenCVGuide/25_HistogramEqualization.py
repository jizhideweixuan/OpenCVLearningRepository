# -*- coding: utf-8 -*-
"""
直方图均衡化
将像素集中在一个范围内的直方图做横向拉伸,
以改善图片对比度
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 全局均化
img = cv2.imread("./DataSource/messi.jpg", 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('res', res)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()


# 自适应均化
# 对于每个小块来说,如果直方图中的 bin 超过对比度的上限的话,
# 就把其中的像素点均匀分散到其他 bins 中,然后在进行直方图均衡化.
# 最后,为了去除每一个小块之间"人造的"（由于算法造成）边界,
# 再使用双线性差值,对小块进行缝合.

# 创建一个clahe对象,tileGridSize 默认小块为8x8
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
res2 = np.hstack((img, cl1))
cv2.imshow('res2', res2)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
