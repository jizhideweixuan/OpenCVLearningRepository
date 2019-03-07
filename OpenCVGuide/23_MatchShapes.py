# -*- coding: utf-8 -*-
"""
形状匹配
函数 cv2.matchShape() 可以帮我们比较两个形状或轮廓的相似度.如
果返回值越小,匹配越好.它是根据 Hu 矩来计算的.文档中对不同的方法都
有解释.
与自己比较的结果是0
"""

import cv2
import numpy as np

img1 = cv2.imread("./DataSource/thunderMin.jpg", 0)
img2 = cv2.imread("./DataSource/thunderBig.jpg", 0)

# 简单阈值
ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
# 取轮廓
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)
