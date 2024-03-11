import cv2

img = cv2.imread('../lenna.png',0)
cv2.imshow('canny',cv2.Canny(img,200,300))
cv2.waitKey()
