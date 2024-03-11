import matplotlib.pyplot as plt
import sklearn.decomposition as DPCA
from sklearn.datasets._base import load_iris

x,y = load_iris(return_X_y=True)#加载数据 return_X_y是否返回数据和标签 x为数据 y为标签
pca = DPCA.PCA(n_components=2)#加载pca算法 设置降成2维
iris = pca.fit_transform(x)#进行降维计算
print(iris)

