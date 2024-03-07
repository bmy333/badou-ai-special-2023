from collections import Counter

import cv2
import numpy as np
import matplotlib.pyplot as plt

def JunHeng(in_ls):
    ls = list(in_ls)
    resls = ls
    image = len(ls)
    Ni = {}
    Pi = {}
    # 求个像素亮度占比
    for i in set(ls):
        Pi[i] = ls.count(i)/ image
    lsum = list(Pi.items())
    spi = Pi
    # 求各元素累加占比
    for sublist in lsum:
        x = 0
        for item in lsum:
            if item <= sublist:
                x += item[1]
            else:
                break
        spi[sublist[0]] = int(x * 256 - 1 if x * 256 - 1 > 0 else 0)
    y = 0
    lu = list(spi.items())
    # 像素原值替换
    for sublist in ls:
        for item in lu:
            if item[0] == sublist:
                resls[y] = item[1]
                break
        y += 1
    return resls

# 列表转图片
def zhuan_image(image, ls):
    h, w = image.shape
    new_img = np.zeros([h, w], dtype=image.dtype)
    x = 0
    for i in range(h):
        for j in range(w):
            new_img[i][j] = ls[x]
            x += 1
    return new_img

img = cv2.imread('../lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
jh = JunHeng(gray.ravel())

plt.figure() #初始化plt画布
plt.subplot(221)
plt.hist(gray.ravel(), bins=256) #原始直方图
plt.subplot(222)
plt.hist(jh , bins=256)
plt.subplot(223)
plt.imshow(gray, cmap='gray')
plt.subplot(224)
plt.imshow(zhuan_image(gray, jh), cmap='gray')
plt.show()