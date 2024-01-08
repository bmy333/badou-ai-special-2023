import cv2
import numpy as np

def ShuanXian(in_img , in_size):
    src_h, src_w, channel = in_img.shape
    new_h, new_w = in_size[0], in_size[1]
    if src_h == new_h and src_w == new_w:
        return in_img.copy()
    new_img = np.zeros(shape=(new_h, new_w, channel), dtype=np.uint8)
    scale_x, scale_y = float(src_w/new_w) , float(src_h/new_h)
    # print('scale_x,',scale_x)
    # print('scale_y,',scale_y)
    for i in range(channel):
        for new_y in range(new_h):
            for new_x in range(new_w):
                # X坐标和Y坐标
                src_x = (new_x+0.5)*scale_x-0.5
                src_y = (new_y+0.5)*scale_y-0.5
                #取4点坐标
                x0 = int(np.floor(src_x))
                x1 = min(x0+1 , src_w-1)
                y0 = int(np.floor(src_y))
                y1 = min(y0+1 , src_h-1)
                temp0 = (x1-src_x) * img[x0,y0,i] + (src_x-x0) * img[x1,y0,i]
                temp1 = (x1-src_x) * img[x1,y0,i] + (src_x-x0) * img[x1,y1,i]
                xx = int((y1-src_y) * temp0 + (src_y-y0) * temp1)
                if xx < 0 :
                    xx = 0
                # print(xx)
                new_img[new_x,new_y,i] = xx
    return new_img



img = cv2.imread('../lenna.png')
in_h , in_w =map(int , input('请输入长宽,并以逗号间隔').split(','))
n_img = ShuanXian(img, [in_h, in_w])
cv2.imshow('test', n_img)
cv2.waitKey()