import numpy as np


class testPCA(object):
    def __init__(self,X,K):#初始化
        self.X = X
        self.K = K
        self.centrX = []
        self.C = []
        self.U = []
        self.Z = []
        self.centrX = self._centr()
        self.C = self._C()
        self.U = self._U()
        self.Z = self._Z()

    def _centr(self):#中心化
        centrX = []
        mean = np.array([np.mean(attr) for attr in self.X.T])#特征均值
        centrX = self.X - mean#中心化
        return centrX

    def _C(self):
        ns = np.shape(self.centrX)[0]#总数
        C = np.dot(self.centrX.T, self.centrX)/ns#协方差矩阵
        return C

    def _U(self):
        a, b = np.linalg.eig(self.C)#特征值和特征向量
        ind = np.argsort(-1*a)#特征值降序索引(不乘-1为升序)
        #构建降维矩阵
        UT = [b[ind[i]] for i in range(self.K)]
        U = np.transpose(UT)
        return U

    def _Z(self):
        Z = np.dot(self.X,self.U)#求降维矩阵
        return Z



X = np.array([[10, 15, 29],
                  [15, 46, 13],
                  [23, 21, 30],
                  [11, 9, 35],
                  [42, 45, 11],
                  [9, 48, 5],
                  [11, 21, 14],
                  [8, 5, 15],
                  [11, 12, 21],
                  [21, 20, 25]])
k = 2
pca = testPCA(X,k)
print(pca.Z)

