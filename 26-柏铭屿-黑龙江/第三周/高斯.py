import cv2
import random
def gausstest(src,means,sigma,bili):
    newimg = src
    x , y = src.shape[:2]
    num = int(bili * x * y)
    for i in range(num):
        randX = random.randint(0,x-1)
        randY = random.randint(0,y-1)
        newimg[randX,randY] = newimg[randX,randY] + random.gauss(means,sigma)
        if newimg[randX,randY] < 0:
            newimg[randX, randY] = 0
        elif newimg[randX,randY] > 255:
            newimg[randX, randY] = 255
    return newimg
img = cv2.imread('../lenna.png',)
img1 = gausstest(img,2,4,0.8)
cv2.imshow('src',img)
cv2.imshow('gauss',img1)
cv2.waitKey()



