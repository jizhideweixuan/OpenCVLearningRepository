# -*- coding: utf-8 -*-
"""
查找轮廓边界框
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/thunderMin.jpg", 0)
# 全局阈值
ret, thresh = cv2.threshold(img, 127, 255, 0)
# 找轮廓
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
# 直边界矩形 一个直矩形（就是没有旋转的矩形）.
# 它不会考虑对象是否旋转,所以边界矩形的面积不是最小的.
# 可以使用函数 cv2.boundingRect() 查找得到.
# （x,y）为矩形左上角的坐标,（w,h）是矩形的宽和高
x, y, w, h = cv2.boundingRect(cnt)
A = img.copy();
A = cv2.rectangle(A, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 旋转的边界矩形 这个边界矩形是面积最小的,因为它考虑了对象的旋转.
# 用到的函数为 cv2.minAreaRect() 返回的是一个 Box2D 结构,
# 其中包含矩形左上角角点的坐标（x,y）,矩形的宽和高（w,h）,以及旋转角度.
# 但是要绘制这个矩形需要矩形的 4 个角点,可以通过函数 cv2.boxPoints() 获得。
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
B = img.copy();
B = cv2.drawContours(B, [box], 0, (0, 0, 255), 2)

# 函数 cv2.minEnclosingCircle() 可以帮我们找到一个对象的外切圆.
# 它是所有能够包括对象的圆中面积最小的一个.
C = img.copy();
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
C = cv2.circle(C, center, radius, (0, 255, 0), 2)

# 椭圆拟合 使用的函数为 cv2.ellipse(),返回值其实就是旋转边界矩形的内切圆
D = img.copy()
ellipse = cv2.fitEllipse(cnt)
D = cv2.ellipse(D, ellipse, (0, 255, 0), 2)

# 直线拟合 我们可以根据一组点拟合出一条直线,同样我们也可以为图像中的白色点拟合出一条直线。
E = img.copy()
rows, cols = E.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
E = cv2.line(E, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

titles = ['Original Image', 'Straight Rectangle', 'Rotated Rectangle',
          'Min Enclosing Circle', 'Fitting an Ellipse', 'Fitting a Line']
images = [img, A, B, C, D, E]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
