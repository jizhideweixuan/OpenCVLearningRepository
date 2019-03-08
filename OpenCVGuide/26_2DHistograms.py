# -*- coding: utf-8 -*-
"""
2D 直方图
使用函数 cv2.calcHist() 来计算直方图(彩色)
记住,计算一维直方图,要从 BGR 转换到 HSV
计算 2D 直方图,函数的参数要做如下修改:
• channels=[0,1] 因为我们需要同时处理 H 和 S 两个通道
• bins=[180,256]H 通道为 180,S 通道为 256。
• range=[0,180,0,256]H 的取值范围在 0 到 180,S 的取值范围在 0 到 256
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/messi.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.imshow('hist', hist)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
