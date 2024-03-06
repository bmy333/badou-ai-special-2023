# encoding=gbk

"""
@author: BraHitYQ
1.Edge detection in the x and y directions of the soft operator����soble����x��y����ı�Ե��⣩
2.Laplacian operator edge detection����laplacian���ӱ�Ե��⣩
3.Canny operator edge detection����canny���ӱ�Ե��⣩
"""


import cv2
from matplotlib import pyplot as plt  

img = cv2.imread("lenna.png", 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  

'''
Sobel����
Sobel���Ӻ���ԭ�����£�
dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) 
ǰ�ĸ��Ǳ���Ĳ�����
��һ����������Ҫ�����ͼ��
�ڶ���������ͼ�����ȣ�-1��ʾ���õ�����ԭͼ����ͬ����ȡ�Ŀ��ͼ�����ȱ�����ڵ���ԭͼ�����ȣ�
dx��dy��ʾ�����󵼵Ľ�����0��ʾ���������û���󵼣�һ��Ϊ0��1��2��
����ǿ�ѡ�Ĳ�����
dst��Ŀ��ͼ��
ksize��Sobel���ӵĴ�С������Ϊ1��3��5��7��
scale�����ŵ����ı���������Ĭ�������û������ϵ����
delta��һ����ѡ������������ӵ����յ�dst�У�ͬ����Ĭ�������û�ж����ֵ�ӵ�dst�У�
borderType���ж�ͼ��߽��ģʽ���������Ĭ��ֵΪcv2.BORDER_DEFAULT��
'''


# �������д���ʹ��Sobel���Ӽ���ͼ����x�����ϵ��ݶȡ�cv2.Sobel()�����Ĳ����������£�
# img_gray������ĻҶ�ͼ��
# cv2.CV_64F�����ͼ����������ͣ�������64λ��������
# 1����ʾ��x�����ϼ����ݶȡ�
# 0����ʾ��y�����ϲ������ݶȡ�
# ksize=3��Sobel���ӵĺ˴�С����������Ϊ3x3��

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)  # ��x��
img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)  # ��y��

# Laplace ����,���д���ʹ��������˹���Ӽ���ͼ��Ķ��׵�������ǰ�������ƣ�
img_laplace = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)  

# Canny ����
# img_gray: ����һ���Ҷ�ͼ�񣬱�ʾ�����ԭʼͼ��
# 100: ����Canny��Ե����㷨��������ֵ����֮һ������ȷ����Ե��ǿ�ȡ���С��ֵ�����¸����ɵı�Ե��⣬�ϴ��ֵ�����¸��ϸ�ı�Ե��⡣
# 150: ����Canny��Ե����㷨����һ����ֵ����֮һ������ȷ����Ե��ǿ�ȡ���С��ֵ�����¸����ɵı�Ե��⣬�ϴ��ֵ�����¸��ϸ�ı�Ե��⡣
img_canny = cv2.Canny(img_gray, 100 , 150)  

plt.subplot(231), plt.imshow(img_gray, "gray"), plt.title("Original")  
plt.subplot(232), plt.imshow(img_sobel_x, "gray"), plt.title("Sobel_x")  
plt.subplot(233), plt.imshow(img_sobel_y, "gray"), plt.title("Sobel_y")  
plt.subplot(234), plt.imshow(img_laplace,  "gray"), plt.title("Laplace")  
plt.subplot(235), plt.imshow(img_canny, "gray"), plt.title("Canny")  
plt.show()  
