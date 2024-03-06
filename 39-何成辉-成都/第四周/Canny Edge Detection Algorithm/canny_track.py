# encoding=gbk


"""
@author: BraHitYQ
Canny edge detection: optimized program����Adjustable threshold range(Canny��Ե��⣺�Ż��ĳ��򡪡��ɵ�����ֵ��Χ),
"""


import cv2


def CannyThreshold(lowThreshold):  
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)  # ��˹�˲�,��һ��ʹ��OpenCV���е�cv2.GaussianBlur�����ԻҶ�ͼ����и�˹ģ������gray������ĻҶ�ͼ��(3, 3)��ʾ��˹�˵Ĵ�СΪ3x3��0��ʾ��׼��Ϊ0�������Ľ���洢�ڱ���detected_edges�С�
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold*ratio, apertureSize=kernel_size)  # ��Ե���,��һ��ʹ��OpenCV���е�cv2.Canny�����Ծ�����˹ģ��������ͼ����б�Ե��⡣detected_edges�������ͼ��lowThreshold��lowThreshold*ratio�ֱ��ʾ����ֵ�͸���ֵ��apertureSize��ʾSobel���ӵĿ׾���С�������Ľ����Ȼ�洢�ڱ���detected_edges�С�

    # just add some colours to edges from original image.
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # ��ԭʼ��ɫ��ӵ����ı�Ե��,��һ��ʹ��OpenCV���е�cv2.bitwise_and������ԭʼͼ�����Ե��������а�λ�������img��ԭʼͼ��mask=detected_edges��ʾʹ�ñ�Ե�������Ϊ���롣�����Ľ���洢�ڱ���dst��
    cv2.imshow('canny demo', dst)  # ��һ��ʹ��OpenCV���е�cv2.imshow������ʾ������ͼ�񡣴��ڱ���Ϊ'canny demo'����ʾ������Ϊ����dst��


#  ȫ�ֱ�������


lowThreshold = 0  
max_lowThreshold = 100  
ratio = 3  
kernel_size = 3  
  
img = cv2.imread('lenna.png')  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ת����ɫͼ��Ϊ�Ҷ�ͼ
  
cv2.namedWindow('canny demo')  
  
# ���õ��ڸ�,
'''
�����ǵڶ���������cv2.createTrackbar()
����5����������ʵ������������������ʹ����֪����ʲô��˼��
��һ�������������trackbar���������
�ڶ��������������trackbar����������������
�����������������trackbar��Ĭ��ֵ,Ҳ�ǵ��ڵĶ���
���ĸ������������trackbar�ϵ��ڵķ�Χ(0~count)
������������ǵ���trackbarʱ���õĻص�������
'''

# ���д��봴����һ�������������ڵ���Canny��Ե����㷨�е���С��ֵ���������ĳ�ʼֵ�ɱ���lowThresholdָ�������ֵ�ɱ���max_lowThresholdָ��������������ֵ�ı�ʱ������ú���CannyThreshold��������ֵ��
cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
# ���д����ʼ����Canny��Ե����㷨����С��ֵΪ0������ͨ������ǰ�涨���CannyThreshold����ʵ�ֵġ�
CannyThreshold(0)  # initialization  
if cv2.waitKey(0) == 27:  # wait for ESC key to exit cv2,���д���ȴ��û�����ESC��������û�������ESC����ASCII��Ϊ27������ִ����һ�д��롣
    cv2.destroyAllWindows()  # ���д���ر����д򿪵Ĵ��ڡ�����δ����У����ر�����ʾCanny��Ե������Ĵ��ڡ�
