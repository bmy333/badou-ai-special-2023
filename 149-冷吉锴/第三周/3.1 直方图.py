import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
calcHist 计算图像直方图
函数原型：calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
images：图像矩阵，例如：[image]
channels：通道数，例如：0
mask：掩膜，一般为：None
histSize：直方图大小，一般等于灰度级数
ranges：横轴范围
"""

# 灰度图像直方图
# 获取灰度图像
img = cv2.imread("lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray", gray)

# 灰度图像的直方图，方法1
plt.figure()
plt.hist(gray.ravel(), 256)  # 绘制直方图,参数bins表示直方图的条形数
plt.show()

# 灰度图像的直方图，方法2
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()  # 新建一个图像
plt.title("Grayscale Histogram")
plt.xlabel("Bins")  # x轴标签
plt.ylabel("Pixels")  # y轴标签
plt.plot(hist)
plt.xlim([0, 256])  # 设置x坐标轴范围
plt.show()

"""
彩色图像直方图
"""

image = cv2.imread("lenna.png")
cv2.imshow("Original", image)
# cv2.waitKey(0)

channels = cv2.split(image)  # 把通道拆开
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")

# 对b，g，r三个通道分别计算直方图
for (chan, color) in zip(channels, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])  # 设置x坐标轴范围
plt.show()
