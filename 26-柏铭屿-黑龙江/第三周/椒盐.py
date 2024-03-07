import cv2
import random

def jytest(src,bili):
    newimg = src
    x , y = src.shape[:2]
    num = int(bili * x * y)
    for i in range(num):
        randX = random.randint(0,x-1)
        randY = random.randint(0,y-1)
        if random.random()<=0.5:
            newimg[randX,randY] = 0
        else:
            newimg[randX, randY] = 255
    return newimg
img = cv2.imread('../lenna.png',0)
img1 = jytest(img,0.2)
img = cv2.imread('../lenna.png',0)
cv2.imshow('src',img)
cv2.imshow('jiaoyan',img1)
cv2.waitKey()

