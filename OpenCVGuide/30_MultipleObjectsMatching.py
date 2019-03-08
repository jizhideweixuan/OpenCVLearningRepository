# -*- coding: utf-8 -*-
"""
多对象模板匹配 cv.imMaxLoc()
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读入原图
img_rgb = cv2.imread("./DataSource/mario.jpg")
# 获得灰度图
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# 读入模板
template = cv2.imread("./DataSource/marioCoin.jpg", 0)
# 获取模板长宽
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# umpy.where(condition[, x, y])
# 返回元素,可以是x或y,具体取决于条件.
# 如果只给出条件,则返回condition.nonzero（）
loc = np.where(res >= threshold)
# 框出给出数据
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
# 展示图片
cv2.imshow('res', img_rgb)
# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
# 保存图片
# cv2.imwrite('res.png', img_rgb)
