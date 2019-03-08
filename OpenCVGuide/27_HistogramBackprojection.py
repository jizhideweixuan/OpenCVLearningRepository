# -*- coding: utf-8 -*-
"""
直方图反向投影
它可以用来做图像分割,或者在图像中找寻我们感兴趣的部分.
简单来说,它会输出与输入图像（待搜索）同样大小的图像,
其中的每一个像素值代表了输入图像上对应点属于目标对象的概率.
用更简单的话来解释,输出图像中像素值越高（越白）的点
就越可能代表我们要搜索的目标（在输入图像所在的位置）

OpenCV 提供的函数 cv2.calcBackProject() 可以用来做直方图反向
投影。它的参数与函数 cv2.calcHist 的参数基本相同.其中的一个参数是我
们要查找目标的直方图.同样再使用目标的直方图做反向投影之前我们应该先
对其做归一化处理.返回的结果是一个概率图像,我们再使用一个圆盘形卷积
核对其做卷操作,最后使用阈值进行二值化.下面就是代码和结果:
"""

import cv2
import numpy as np

# 查找目标读入
roi = cv2.imread("./DataSource/green.jpg")
# 转换成HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 源图片读入
target = cv2.imread("./DataSource/messi.jpg")
# 转换成HSV
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# 计算直方图
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# 归一化:原始图像,结果图像,映射到结果图像中的最小值,最大值,归一化类型
# cv2.NORM_MINMAX 对数组的所有值进行转化,使它们线性映射到最小值和最大值之间
# 归一化之后的直方图便于显示,归一化之后就成了 0 到 255 之间的数了
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)
# 阈值和二进制AND操作
ret, thresh = cv2.threshold(dst, 50, 255, 0)
# 别忘了是三通道图像,因此这里使用 merge 变成 3 通道
thresh = cv2.merge((thresh, thresh, thresh))
# 按位操作
res = cv2.bitwise_and(target, thresh)
res = np.hstack((target, thresh, res))
# 显示图像
cv2.imshow('res', res)
cv2.waitKey(0)
