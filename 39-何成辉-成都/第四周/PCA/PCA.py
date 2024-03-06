# encoding=gbk

"""
@author: BraHitYQ
Use PCA (Principal Component Analysis) to reduce the dimensionality of the Iris dataset and visualize the results.(ʹ��PCA�����ɷַ��������β�����ݼ����н�ά������������ӻ�)
"""

"""
scatter�����Ĳ������£�
    x��x���ϵ����ݵ㡣
    y��y���ϵ����ݵ㡣
    s��ɢ��Ĵ�С��Ĭ��ΪNone��
    c��ɢ�����ɫ��Ĭ��ΪNone��
    marker��ɢ��ı����ʽ��Ĭ��ΪNone��
    cmap����ɫӳ�䣬Ĭ��ΪNone��
    norm����һ������Ĭ��ΪNone��
    vmin����ɫӳ�����Сֵ��Ĭ��ΪNone��
    vmax����ɫӳ������ֵ��Ĭ��ΪNone��
    alpha��ɢ���͸���ȣ�Ĭ��ΪNone��
    linewidths��ɢ����߿�Ĭ��ΪNone��
    edgecolors��ɢ��ı�Ե��ɫ��Ĭ��ΪNone��
    plotnonfinite���Ƿ���Ʒ�����ֵ�����ݣ�Ĭ��ΪFalse��
    data������Դ��Ĭ��ΪNone��
    **kwargs�������ؼ��ֲ�����
"""

import matplotlib.pyplot as plt
import sklearn.decomposition as dp
from sklearn.datasets._base import load_iris  # ��sklearn���datasetsģ���е���load_iris���������ڼ����β�����ݼ���

x, y = load_iris(return_X_y=True)  # �������ݣ�x��ʾ���ݼ��е��������ݣ�y��ʾ���ݱ�ǩ,����load_iris���������β�����ݼ���������������x��Ŀ������y�ֱ�ֵ������x��y��
pca = dp.PCA(n_components=2)  # ����pca�㷨,����һ��PCA����,���ý�ά�����ɷ���ĿΪ2
reduced_x = pca.fit_transform(x)  # ʹ��PCA�������������x���н�ά������ά��Ľ����ֵ������reduced_x��
red_x, red_y = [], []  # ����2�����б����ڴ洢��ͬ���Ľ�ά�������ֵ
blue_x, blue_y = [], []
green_x, green_y = [], []
for i in range(len(reduced_x)):  # ������ά�����������reduced_x�ĳ���.�����β������𽫽�ά������ݵ㱣���ڲ�ͬ�ı��У�
    if y[i] == 0:  # �ж�Ŀ������y�ĵ�i��Ԫ���Ƿ����0��
        red_x.append(reduced_x[i][0])  # �������0���򽫽�ά�������ֵ�ĵ�һ��������ӵ�red_x�б��С�
        red_y.append(reduced_x[i][1])  # �������0���򽫽�ά�������ֵ�ĵڶ���������ӵ�red_y�б��С�
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])  # �������1���򽫽�ά�������ֵ�ĵ�һ��������ӵ�blue_x�б��С�
        blue_y.append(reduced_x[i][1])  # �������1���򽫽�ά�������ֵ�ĵڶ���������ӵ�blue_y�б��С�
    else:
        green_x.append(reduced_x[i][0])  # ����ά�������ֵ�ĵ�һ��������ӵ�green_x�б��С�
        green_y.append(reduced_x[i][1])  # ����ά�������ֵ�ĵڶ���������ӵ�green_y�б��С�
plt.scatter(red_x, red_y, c='r', marker='x')  # ʹ��matplotlib��scatter�������ƺ�ɫx��ǵ�ɢ��ͼ����ʾ���0�����ݡ�
plt.scatter(blue_x, blue_y, c='b', marker='D')  # ʹ��matplotlib��scatter����������ɫD��ǵ�ɢ��ͼ����ʾ���1�����ݡ�
plt.scatter(green_x, green_y, c='g', marker='.')  # ʹ��matplotlib��scatter����������ɫ���ǵ�ɢ��ͼ����ʾ���2�����ݡ�
plt.show()
