# -*- coding: utf-8 -*-
"""
轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线,具有相同的颜色或者灰度.
轮廓在形状分析和物体的检测和识别中很有用.
    1.为了更加准确,要使用二值化图像.
        在寻找轮廓之前,要进行阈值化处理,或者 Canny 边界检测.
    2.查找轮廓的函数会修改原始图像,如果你在找到轮廓之后还想使用原始图像的话,
        你应该将原始图像存储到其他变量中.
    3.在 OpenCV 中,查找轮廓就像在黑色背景中超白色物体.你应该记住,
        要找的物体应该是白色而背景应该是黑色.

让我们看看如何在一个二值图像中查找轮廓:
    函数 cv2.findContours() 有三个参数,第一个是输入图像,第二个是轮廓检索模式,第三个是轮廓近似方法.
    返回值有三个,第一个是图像,第二个是轮廓,第三个是（轮廓的）层析结构.
    轮廓（第二个返回值）是一个 Python列表,其中存储这图像中的所有轮廓.
    每一个轮廓都是一个 Numpy 数组,包含对象边界点（x,y）的坐标.

    函数 cv2.drawContours() 可以被用来绘制轮廓.
    它可以根据你提供的边界点绘制任何形状.
    它的第一个参数是原始图像,第二个参数是轮廓，一个 Python 列表.
    第三个参数是轮廓的索引在绘制独立轮廓是很有用，当设置为 -1 时绘制所有轮廓）.
    接下来的参数是轮廓的颜色和厚度等。
"""

import numpy as np
import cv2

img = cv2.imread("./DataSource/1.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# 轮廓近似: cv2.CHAIN_APPROX_NONE 存储所有的边界点,但很多时候我们不需要
# cv2.CHAIN_APPROX_SIMPLE 取出冗余节省开支
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
A = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# 和前者一样,但是这个更加有用
B = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
# cv2.imshow('A', A)
cv2.imshow('B', B)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
