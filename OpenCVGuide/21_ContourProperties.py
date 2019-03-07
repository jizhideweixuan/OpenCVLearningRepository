# -*- coding: utf-8 -*-
"""
轮廓的性质
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/thunderMin.jpg", cv2.IMREAD_GRAYSCALE)
# 全局阈值
ret, thresh = cv2.threshold(img, 127, 255, 0)
# 找轮廓
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
# 面积
area = cv2.contourArea(cnt)
# 取得矩形坐标
x, y, w, h = cv2.boundingRect(cnt)

# 长宽比
aspect_ratio = float(w) / h
print("长宽比 ", aspect_ratio)

# 轮廓面积与边界矩形面积的比
rect_area = w * h
extent = float(area) / rect_area
print("轮廓面积与边界矩形面积的比 ", extent)

# 轮廓面积与凸包面积的比
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area
print("轮廓面积与凸包面积的比 ", solidity)

#  与轮廓面积相等的圆形的直径
equi_diameter = np.sqrt(4 * area / np.pi)
print("与轮廓面积相等的圆形的直径 ", equi_diameter)

# 方向
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)

# 掩模img输入要是灰度图
mask = np.zeros(img.shape, np.uint8)
# 这里一定要使用参数-1, 绘制填充的的轮廓
cv2.drawContours(mask, [cnt], 0, 255, -1)
# 像素点
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)

# 最大值和最小值,利用掩模计算得出,img输入为灰度图
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask=mask)
print(" min_val:", min_val, " max_val:", max_val,
      " min_loc:", min_loc, " max_loc:", max_loc)

# 平均颜色及平均灰度
mean_val = cv2.mean(img, mask=mask)
print("平均颜色及平均灰度 ", mean_val)

# 极点
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print(" leftmost:", leftmost, " rightmost:", rightmost,
      " topmost:", topmost, " bottommost:", bottommost)

#   求解图像中的一个点到一个对象轮廓的最短距离.如果点在轮廓的外部,
# 返回值为负.如果在轮廓上，返回值为 0.如果在轮廓内部,返回值为正.
# 下面我们以点（50，50）为例:
#   此函数的第三个参数是 measureDist.
# 如果设置为 True,就会计算最短距离.
# 如果是 False,只会判断这个点与轮廓之间的位置关系（返回值为 +1,-1,0）.
dist = cv2.pointPolygonTest(cnt, (50, 50), True)
print("点到轮廓的最短距离 ", dist)
