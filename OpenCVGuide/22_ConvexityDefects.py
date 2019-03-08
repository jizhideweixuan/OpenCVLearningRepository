# -*- coding: utf-8 -*-
"""
凸缺陷
"""
import cv2
import numpy as np

# 读图
img = cv2.imread("./DataSource/thunderMin.jpg")
# 取灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 简单阈值
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
# 取轮廓
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

"""
OpenCV 中有一个函数 cv.convexityDefect() 可以帮助我们找到凸缺陷.函数调用如下:
如果要查找凸缺陷，在使用函数 cv2.convexHull 找凸包时,参数returnPoints 一定要是 False
它会返回一个数组,其中每一行包含的值是 [起点,终点,最远的点,到最远点的近似距离]
我们可以在一张图上显示它,我们将起点和终点用一条绿线连接,在最远点画一个圆圈,
要记住的是返回结果的前三个值是轮廓点的索引.所以我们还要到轮廓点中去找它们.
"""

# 取凸包
hull = cv2.convexHull(cnt, returnPoints=False)
# 找到突缺陷
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
