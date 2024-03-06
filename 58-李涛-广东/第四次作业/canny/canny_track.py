#!/usr/bin/env python
# encoding=gbk

import cv2
import numpy as np

'''
Canny��Ե��⣺�Ż��ĳ���
'''

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3


def CannyThreshold(lowThreshold):
    """
    ��˹�˲�����ȥ����ͼ���е��ӵĸ�Ƶ����
    ��һ�������������ͼ��������gray����ʾ�ԻҶ�ͼ����и�˹ģ������
    �ڶ��������Ǹ�˹�˵Ĵ�С��������(3, 3)����ʾ��˹�˵Ŀ�͸߶�Ϊ3��
    ������������X��Y�����ϵı�׼�������0����ʾ��X��Y�����ϵı�׼�Ϊ0����ʾ�Զ����ݸ�˹�˵Ĵ�С�����׼�
    """
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)

    """
    cv2.bitwise_and:
    ��һ���͵ڶ����������������ͼ�����ﶼ��img����ʾ��ԭʼͼ��img���а�λ�������
    mask����ָ����ҪӦ�õ����룬��detected_edges����ʾʹ��detected_edges��Ϊ������а�λ�������
    """
    dst = cv2.bitwise_and(img, img, mask=detected_edges)
    cv2.imshow('canny demo', dst)


img = cv2.imread('b.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('canny demo')

'''
createTrackbar���������������£�
trackbarName�������������ƣ���һ���ַ�����
windowName�������������Ĵ������ƣ���һ���ַ�����
value���������ĳ�ʼֵ��ͨ����һ��������
count�������������ֵ��ͨ����һ��������
onChange���ص�����������������ֵ�����仯ʱ����øú�����
ͨ��ʹ��createTrackbar������������OpenCV�Ĵ����д��������������ڻ�������ֵ�仯ʱִ����ز����������ͼ����Ĳ�����������ʾ�ȡ�
'''
cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization  
if cv2.waitKey(0) == 27:  # wait for ESC key to exit cv2
    cv2.destroyAllWindows()
