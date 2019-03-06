# -*- coding: utf-8 -*-
"""
转换颜色空间
"""
import cv2
from matplotlib import pyplot as plt

# 转换颜色空间,常用BGR-GRAY,BGR-HSV,注意opencv的HSV,色度H[0,179],饱和度S[0,255],亮度V[0,255]
# 输出所有可用的flag
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
img = cv2.imread("./DataSource/1.jpg", cv2.IMREAD_COLOR)
# BGR-GRAY cv2.COLOR_BGR2GRAY BGR-HSV cv2.COLOR_BGR2HSV
cv2.imshow('GRAY', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.imshow('HSV', cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
# 使用matplotlib,要进行归一化 img[:, :, [2, 1, 0]]
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:, :, [2, 1, 0]]), plt.title('1')
plt.show()

key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
