# -*- coding: utf-8 -*-
"""
Gui
"""
import cv2

# 图片的读取,显示,窗口注销

# 读取图片
# cv2.IMREAD_COLOR：读入彩色图像,透明度会被忽略,这是默认参数
# cv2.IMREAD_GRAYSCALE：以灰度模式读入
# cv2.IMREAD_UNCHANGED：读入图像,包括alpha
# -1 解码方式
# 0单通道方式
# 3通道方式
img = cv2.imread("./DataSource/1.jpg", cv2.IMREAD_COLOR)
# 可以创建多个窗口,但是名字必须不同
cv2.imshow('img', img)

# 无限等待键盘输入
key = cv2.waitKey(0) & 0xFF
# 按下esc
if key == 27:
    # 销毁所有窗口
    cv2.destroyAllWindows()
# 按下s
elif key == ord('s'):
    # 保存图像
    cv2.imwrite('saveTest.jpg', img)
