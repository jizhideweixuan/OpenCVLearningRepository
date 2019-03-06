# -*- coding: utf-8 -*-
"""
基本操作
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/1.jpg", cv2.IMREAD_COLOR)
# 可以创建多个窗口,但是名字必须不同

# 获取图像属性
# 返回行数,列数,元数
print("行数,列数,元数: ", img.shape)
# 返回图像类型
print("类型: ", img.dtype)

# 获取RGB值
rgb = img[100, 100]
print("RGB: ", rgb)
# 获取灰度值
gray = img[100, 100, 0]
print("Gray: ", gray)

# 扩边
img1 = img
BLUE = [255, 0, 0]
# cv2.BORDER_CONSTANT 以特定颜色扩边
# 参数:源,top,bottom,left,right,目标,颜色
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, img1, BLUE)
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()

# 通道分离
img2 = img
# 将三个通道分离,这是一个非常耗时的操作,尽量使用numpy索引
b, g, r = cv2.split(img2)
# 将三个通道合并
img2 = cv2.merge((b, g, r))
# numpy索引,获得b
b = img2[:, :, 0]
# numpy索引,红色通道设置为0
img2[:, :, 2] = 0
cv2.imshow('red0', img2)
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
