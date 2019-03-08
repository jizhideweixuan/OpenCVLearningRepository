# -*- coding: utf-8 -*-
"""
统计直方图(根据灰度图绘制)
BINS:上面的直方图显示了每个灰度值对应的像素数
DIMS:表示我们收集数据的参数数目
RANGE:就是要统计的灰度值范围,一般来说为 [0，256],也就是说所有的灰度值

使用 OpenCV 统计直方图 函数 cv2.calcHist 可以帮助我们统计一幅图像的直方图
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
images: 原图像（图像格式为 uint8 或 float32）.当传入函数时应该用中括号 [] 括起来,例如:[img]
channels: 同样需要用中括号括起来,它会告诉函数我们要统计那幅图像的直方图.
        如果输入图像是灰度图,它的值就是 [0] 如果是彩色图像的话,传入的参数可以是 [0],[1],[2] 它们分别对应着通道 B,G,R
mask: 掩模图像.要统计整幅图像的直方图就把它设为 None 但是如果你想统计图像某一部分的直方图的话,你就需要制作一个掩模图像,
     并使用它.
histSize:BIN 的数目.也应该用中括号括起来,例如:[256]
ranges: 像素值范围,通常为 [0,256]

img = cv2.imread('home.jpg',0)
# 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
hist = cv2.calcHist([img],[0],None,[256],[0,256])
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/messi.jpg")

# 使用 matplotlib.pyplot.hist()
plt.hist(img.ravel(), 256, [0, 256]);
plt.show()

# 使用cv2.calcHist()
color = ('b', 'g', 'r')
# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置 enumerrate 函数会有更加直接，优美的做法
# enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
plt.plot(histr, color=col)
plt.xlim([0, 256])
plt.show()

# 使用掩模
# 要统计图像某个局部区域的直方图只需要构建一副掩模图像.
# 将要统计的部分设置成白色,其余部分为黑色,然后把这个掩模图像传给函数就可以了.
# 创建掩模
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
# 利用掩模创建直方图 和不用掩模创建直方图
# 第三个参数为掩模
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])
plt.show()
