'''
第二周作业1
分别用cv2和plt导入的图片
实现灰度化和二值化
'''
import numpy as np
import cv2
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


# 暴力修改图片尺寸
def KuoDa(in_img, img_size):
    src_h, src_w, channel = in_img.shape
    new_h, new_w = img_size[0], img_size[1]
    if src_h == new_h and src_w == new_w:
        return in_img
    # print('您输入的长宽是:', new_h, new_w)
    new_img = np.zeros(shape=(new_h, new_w, channel), dtype=np.uint8)
    xishu_h = src_h / new_h
    xishu_w = float(src_w / new_w)
    # print(xishu_w,xishu_h)
    for i in range(channel):
        for new_img_h in range(new_h):
            for new_img_w in range(new_w):
                s_h = new_img_h * xishu_h
                s_w = new_img_w * xishu_w
                # print(s_h,s_w)
                new_img[new_img_h, new_img_w, i] = in_img[int(s_h + 0.5), int(s_w + 0.5), i]
                # print(i,new_img_h,new_img_w)
    return new_img

img = cv2.imread('lenna.png')
# cv2.imshow('test',img)
# print(img.shape)
# in_h , in_w =map(int , input('请输入长宽,并以逗号间隔').split(','))
# new = KuoDa(img,[in_h,in_w])
# cv2.imshow('kuoda',new)
# cv2.waitKey()

# 图片灰度化
def huidu(in_img):
    h, w = in_img.shape[: 2]
    # print( h , w)
    hui_img = np.zeros([h, w], dtype=in_img.dtype)
    for i in range(h):
        for j in range(w):
            n = in_img[i, j]
            hui_img[i, j] = int(n[0] * 0.11 + n[1] * 0.59 + n[2] * 0.3)
    return hui_img


# 图片二值化
# plt方法导入图片后 灰度化处理作为输入
def erzhi(in_img):
    h, w = in_img.shape
    hui_img = np.zeros([h, w], dtype=in_img.dtype)
    for i in range(h):
        for j in range(w):
            if in_img[i, j] >= 0.5:
                hui_img[i, j] = 1
            else:
                hui_img[i, j] = 0
    return hui_img


# 图片二值化
# cv2灰度化处理后作为输入
def erzhi2(in_img):
    h, w = in_img.shape
    hui_img = np.zeros([h, w], dtype=in_img.dtype)
    for i in range(h):
        for j in range(w):
            if in_img[i, j] >= 128:
                hui_img[i, j] = 255
            else:
                hui_img[i, j] = 0
    return hui_img



# cv2二值化实现方法
hui_img = huidu(img)
cv2.imshow('erzhi_cv2', erzhi2(hui_img))

# plt二值化实现方法
plt_img = plt.imread('lenna.png')
r2gray_img = rgb2gray(plt_img)
cv2.imshow('test', r2gray_img)
cv2.imshow('erzhi', erzhi(r2gray_img))
plt.subplot(221)
plt.imshow(plt_img)
plt.subplot(222)
plt.imshow(r2gray_img, cmap='gray')
plt.subplot(223)
plt.imshow(np.where(r2gray_img >= 0.5, 1, 0), cmap='gray')
plt.show()
cv2.waitKey()


