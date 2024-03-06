#!/usr/bin/env python
# encoding=gbk

import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = [u'SimHei']

img_input = cv2.imread("lenna.png", 1)

# cv2�Ĳ�ɫת�Ҷ�ͼ
img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
output = cv2.Canny(img_gray, 250, 300)

plt.subplot(121), plt.title("ԭʼ�Ҷ�ͼ")
plt.imshow(img_gray, cmap='gray')
plt.subplot(122), plt.title("ԭʼ�Ҷ�ͼ")
plt.imshow(output, cmap='gray')
plt.show()