# encoding=gbk

"""
@author: BraHitYQ
Canny edge detection(Canny��Ե���)����Canny�������ڱ�Ե��⣬��ͨ������ͼ����ÿ�����ص���ݶ�ǿ�Ⱥͷ���������Ե��
The Canny function is used for edge detection, which detects edges by calculating the gradient intensity and direction of each pixel in the image.
"""


import cv2


'''
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])   
��Ҫ������
    image������ͼ������Ϊcv2.typing.MatLike���ò�������Ҫ�����ԭͼ�񣬸�ͼ�����Ϊ��ͨ���ĻҶ�ͼ��
    threshold1����һ����ֵ������Ϊfloat���ò������ͺ���ֵ1��
    threshold2���ڶ�����ֵ������Ϊfloat���ò������ͺ���ֵ2��
    edges�������Եͼ������Ϊcv2.typing.MatLike | None��Ĭ��ֵΪNone��
    apertureSize����˹ģ���Ŀ׾���С������Ϊint��Ĭ��ֵΪ3��
    L2gradient���Ƿ�ʹ��L2���������ݶȣ�����Ϊbool��Ĭ��ֵΪFalse��
    
�������ܣ�
    ��������һ������Ϊcv2.typing.MatLike�ı�Եͼ���ں����ڲ����������Ƚ�����ͼ��ת��Ϊ�Ҷ�ͼ�������δת������Ȼ��ʹ�ø�˹ģ����ͼ�����ƽ�����������������ǵ���cv2.Canny()����������Ե����������洢��detected_edges�����С�������Ƿ��ؼ�⵽�ı�Եͼ��
'''


img = cv2.imread("lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # ��ʵ�ò������ȡ������Ϊcanny�����Դ�ͼ��ҶȻ�
cv2.imshow("canny", cv2.Canny(gray, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()


"""
���������
    1.����cv2��
    2.ʹ��cv2.imread()������ȡͼƬ������1��ʾ�Բ�ɫģʽ��ȡͼƬ
    3.ʹ��cv2.cvtColor()��������ɫͼ��ת��Ϊ�Ҷ�ͼ��
    4.ʹ��cv2.Canny()��������Canny��Ե��⣬����200��300�ֱ��ʾ����ֵ�͸���ֵ
    5.ʹ��cv2.imshow()������ʾ������ͼ��
    6.ʹ��cv2.waitKey()�����ȴ��û�����
    7.ʹ��cv2.destroyAllWindows()�����ر����д򿪵Ĵ���
"""