# -*- coding: utf-8 -*-
"""
傅里叶变换经常被用来分析不同滤波器的频率特性
DFT: 2D 离散傅里叶变换,用于分析图像的领域特性,其中快速傅里叶变换称为FFT
对于一个正弦信号,如果它的幅度变化非常快,我们可以说他是高频信号,
如果变化非常慢,我们称之为低频信号.
你可以把这种想法应用到图像中,图像那里的幅度变化非常大呢?边界点或者噪声.
所以我们说边界和噪声是图像中的高频分量（注意这里的高频是指变化非常次数多）.
如果没有如此大的幅度变化我们称之为低频分量.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./DataSource/messi.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
