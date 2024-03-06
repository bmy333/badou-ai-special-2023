import numpy as np
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pic_path = 'lenna.png'
    img = plt.imread(pic_path)
    # print(img)
    # print(img.shape)  # [512, 512, 3]
    if pic_path[-4:] == '.png':  # .png图片在这里的存储格式是0到1的浮点数，所以要扩展到255再计算
        img = img * 255  # 还是浮点数类型
    img = img.mean(axis=-1)  # 取均值就是灰度化了

    '''1、高斯平滑'''
    # sigma = 1.52  # 高斯平滑时的高斯核参数，标准差，可调
    sigma = 0.5  # 高斯平滑时的高斯核参数，标准差，可调
    # 一般给定σ，则k取2×3σ+1，因为 (-3σ, 3σ) 恰好包含了高斯分布的主要部分
    dim = int(np.round(6 * sigma + 1))  # round是四舍五入函数，根据标准差求高斯核是几乘几的，也就是维度
    if dim % 2 == 0:  # 最好是奇数，不是的话加一
        dim += 1
    Gaussian_filter = np.zeros([dim, dim])  # 存储高斯核，这是数组不是列表了
    tmp = [i - dim // 2 for i in range(dim)]  # 生成一个序列，用来生成高斯滤波的的序列：高斯函数中的X,Y从这个序列中取
    n1 = 1 / (2 * math.pi * sigma ** 2)  # 计算高斯核
    n2 = -1 / (2 * sigma ** 2)
    for i in range(dim):
        for j in range(dim):
            Gaussian_filter[i, j] = n1 * math.exp(n2 * (tmp[i] ** 2 + tmp[j] ** 2))
    Gaussian_filter = Gaussian_filter / Gaussian_filter.sum()  # 除以本身的和，即归一化
    dx, dy = img.shape
    img_new = np.zeros(img.shape)  # 存储平滑之后的图像，zeros函数得到的是浮点型数据
    tmp = dim // 2  # 高斯滤波的半径,用来进行边缘填补
    img_pad = np.pad(img, ((tmp, tmp), (tmp, tmp)), 'constant')  # 边缘填补
    for i in range(dx):
        for j in range(dy):
            img_new[i, j] = np.sum(img_pad[i:i + dim, j:j + dim] * Gaussian_filter)  # 做卷积，加权求和
    plt.figure(1)
    plt.imshow(img_new.astype(np.uint8), cmap='gray')  # 此时的img_new是255的浮点型数据，强制类型转换才可以
    plt.axis('off')  # 关闭坐标轴

    '''2、求梯度  以下两个是滤波求梯度用的sobel矩阵（检测图像中的水平、垂直和对角边缘）'''
    sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    img_tidu_x = np.zeros(img_new.shape)  # 存储梯度图像
    img_tidu_y = np.zeros([dx, dy])
    img_tidu = np.zeros(img_new.shape)
    img_pad = np.pad(img_new, ((1, 1), (1, 1)), 'constant')  # 边缘填补，根据上面矩阵结构所以写1
    for i in range(dx):
        for j in range(dy):
            # print(img_pad[i + 1, j + 1])
            # print(img_pad[i:i + 3, j:j + 3])  # 扩充后的8邻域
            img_tidu_x[i, j] = np.sum(img_pad[i:i + 3, j:j + 3] * sobel_kernel_x)  # x方向卷积
            img_tidu_y[i, j] = np.sum(img_pad[i:i + 3, j:j + 3] * sobel_kernel_y)  # y方向卷积
            img_tidu[i, j] = np.sqrt(img_tidu_x[i, j] ** 2 + img_tidu_y[i, j] ** 2)  # 斜边卷积
    img_tidu_x[img_tidu_x == 0] = 0.00000001  # 防止被除数为0
    angle = img_tidu_y / img_tidu_x  # 计算角度
    plt.figure(2)
    plt.imshow(img_tidu.astype(np.uint8), cmap='gray')
    plt.axis('off')

    '''3、非极大值抑制'''
    img_yizhi = np.zeros(img_tidu.shape)
    # 为什么是1到dx-1，因为是八邻域比较，所以从横纵坐标都是第二个开始，从横纵坐标都是倒数第二个结束，就能比较所有的点
    for i in range(1, dx-1):
        for j in range(1, dy-1):
            flag = True  # 在8邻域内是否要抹去做个标记
            # print(img_tidu)
            # print(img_tidu[i - 1:i + 2, j - 1:j + 2])
            temp = img_tidu[i - 1:i + 2, j - 1:j + 2]  # 梯度幅值的8邻域矩阵
            if angle[i, j] <= -1:  # 使用线性插值法判断抑制与否(tanh值) 梯度方向：左上和右下
                # print(temp)
                # print(temp[0, 1], temp[0, 0])
                num_1 = (temp[0, 1] - temp[0, 0]) / angle[i, j] + temp[0, 1]
                num_2 = (temp[2, 1] - temp[2, 2]) / angle[i, j] + temp[2, 1]
                if not (img_tidu[i, j] > num_1 and img_tidu[i, j] > num_2):
                    flag = False
            elif angle[i, j] >= 1:  # 梯度方向：右上和左下
                num_1 = (temp[0, 2] - temp[0, 1]) / angle[i, j] + temp[0, 1]
                num_2 = (temp[2, 0] - temp[2, 1]) / angle[i, j] + temp[2, 1]
                if not (img_tidu[i, j] > num_1 and img_tidu[i, j] > num_2):
                    flag = False
            elif angle[i, j] > 0:  # 梯度方向：右边和左边
                num_1 = (temp[0, 2] - temp[1, 2]) * angle[i, j] + temp[1, 2]
                num_2 = (temp[2, 0] - temp[1, 0]) * angle[i, j] + temp[1, 0]
                if not (img_tidu[i, j] > num_1 and img_tidu[i, j] > num_2):
                    flag = False
            elif angle[i, j] < 0:  # 梯度方向：上边和下边
                num_1 = (temp[1, 0] - temp[0, 0]) * angle[i, j] + temp[1, 0]
                num_2 = (temp[1, 2] - temp[2, 2]) * angle[i, j] + temp[1, 2]
                if not (img_tidu[i, j] > num_1 and img_tidu[i, j] > num_2):
                    flag = False
            if flag:
                img_yizhi[i, j] = img_tidu[i, j]
    plt.figure(3)
    plt.imshow(img_yizhi.astype(np.uint8), cmap='gray')
    plt.axis('off')

    '''4、双阈值检测，连接边缘。遍历所有一定是边的点，查看8邻域是否存在有可能是边的点，进栈'''
    lower_boundary = img_tidu.mean() * 0.5  # 经验设定的,通用的
    high_boundary = lower_boundary * 3  # 这里设置高阈值是低阈值的3倍（经验设定的）
    zhan = []
    for i in range(1, img_yizhi.shape[0] - 1):  # 外圈不考虑了
        for j in range(1, img_yizhi.shape[1] - 1):
            # 大于高阈值的点一定是强边缘点
            if img_yizhi[i, j] >= high_boundary:  # 取，一定是边的点
                img_yizhi[i, j] = 255
                zhan.append([i, j])
            # 小于低阈值的点一定不是边缘点
            elif img_yizhi[i, j] <= lower_boundary:  # 舍
                img_yizhi[i, j] = 0

    # 此时只处理了大于高阈值和小于低阈值的点，处于阈值中间的点没有处理

    while not len(zhan) == 0:
        temp_1, temp_2 = zhan.pop()  # 出栈
        a = img_yizhi[temp_1 - 1:temp_1 + 2, temp_2 - 1:temp_2 + 2]  # 当前要算的区域
        # print(a)
        if (a[0, 0] < high_boundary) and (a[0, 0] > lower_boundary):
            img_yizhi[temp_1 - 1, temp_2 - 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 - 1, temp_2 - 1])  # 进栈
        if (a[0, 1] < high_boundary) and (a[0, 1] > lower_boundary):
            img_yizhi[temp_1 - 1, temp_2] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 - 1, temp_2])  # 进栈
        if (a[0, 2] < high_boundary) and (a[0, 2] > lower_boundary):
            img_yizhi[temp_1 - 1, temp_2 + 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 - 1, temp_2 + 1])  # 进栈
        if (a[1, 0] < high_boundary) and (a[1, 0] > lower_boundary):
            img_yizhi[temp_1, temp_2 - 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1, temp_2 - 1])  # 进栈
        if (a[1, 2] < high_boundary) and (a[1, 2] > lower_boundary):
            img_yizhi[temp_1, temp_2 + 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1, temp_2 + 1])  # 进栈
        if (a[2, 0] < high_boundary) and (a[2, 0] > lower_boundary):
            img_yizhi[temp_1 + 1, temp_2 - 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 + 1, temp_2 - 1])  # 进栈
        if (a[2, 1] < high_boundary) and (a[2, 1] > lower_boundary):
            img_yizhi[temp_1 + 1, temp_2] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 + 1, temp_2])  # 进栈
        if (a[2, 2] < high_boundary) and (a[2, 2] > lower_boundary):
            img_yizhi[temp_1 + 1, temp_2 + 1] = 255  # 这个像素点标记为边缘
            zhan.append([temp_1 + 1, temp_2 + 1])  # 进栈

    # 剩下的大于低阈值和小于高阈值的点就是孤立的点，舍弃掉，做完之后还是弱边缘的就删了
    for i in range(img_yizhi.shape[0]):
        for j in range(img_yizhi.shape[1]):
            if img_yizhi[i, j] != 0 and img_yizhi[i, j] != 255:
                img_yizhi[i, j] = 0

    # 绘图
    plt.figure(4)
    plt.imshow(img_yizhi.astype(np.uint8), cmap='gray')
    plt.axis('off')
    plt.show()

