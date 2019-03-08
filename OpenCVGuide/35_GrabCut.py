# -*- coding: utf-8 -*-
"""
cv2.grabCut()
img - 输入图像
• mask-掩模图像,用来确定那些区域是背景,前景,可能是前景/背景等.
    可以设置为：cv2.GC_BGD,cv2.GC_FGD,cv2.GC_PR_BGD,cv2.GC_PR_FGD，
    或者直接输入 0,1,2,3 也行.
• rect - 包含前景的矩形，格式为 (x,y,w,h)
• bdgModel, fgdModel - 算法内部使用的数组. 你只需要创建两个大
    小为 (1,65),数据类型为 np.float64 的数组.
• iterCount - 算法的迭代次数
• mode 可以设置为 cv2.GC_INIT_WITH_RECT 或 cv2.GC_INIT_WITH_MASK,
    也可以联合使用.这是用来确定我们进行修改的方式,矩形模式或者掩模模式.
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/messi.jpg")
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 450, 290)
# 函数的返回值是更新的 mask, bgdModel, fgdModel
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
