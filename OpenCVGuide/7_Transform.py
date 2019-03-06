# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("./DataSource/1.jpg", 0)

# 缩放
# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子,因此这里为 None
#  缩小: cv2.INTER_AREA 放大: v2.INTER_CUBIC（慢) v2.INTER_LINEAR (默认)
res = cv2.resize(img, None, 1, 2, cv2.INTER_CUBIC)
# OR
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height, width = img.shape[:2]
res = cv2.resize(img, (1 * width, 2 * height), cv2.INTER_CUBIC)

# 旋转
rows, cols = img.shape
# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (cols, rows))

while (1):
    cv2.imshow('res', res)
    cv2.imshow('dst', dst)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
