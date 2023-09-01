#  Copyright (c) 2022. Generated by Gu.
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from numpy import random

seaborn.set()  # 设置画图风格
X = random.rand(10, 2)
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()

# 两点距离的平方等于每个维度的距离差的平方的和。
# 利用NumPy的广播和聚合功能用一行代码计算矩阵的平方距离:
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)
nearest = np.argsort(dist_sq, axis=1)
print(nearest)

# #在坐标系中计算每对点的差值
# differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
# differences.shape
#
# #求出差值的平方
# sq_differences = differences ** 2
# sq_differences.shape
#
# #将差值求和获得平方距离
# dist_sq = sq_differences.sum(-1)
# dist_sq.shape

# 该矩阵的对角线(也就是每个点到其自身的距离)的值都是0
# dist_sq.diagonal()

# 当我们有了这样一个转化为两点间的平方距离的矩阵后,就可以使用
# np.argsort()函数沿着每行进行排序了。最左边的列给出的索引值就是最近邻:
# 第一列是按0~9从小到大排列的。这是因为每个点的最近邻是其自身
nearest = np.argsort(dist_sq, axis=1)
print(nearest)

# 分隔每一行,这样最小的k+1的平方距离将排在最前面,其他更长的距离占据矩阵该行的其他位置
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

plt.scatter(X[:, 0], X[:, 1], s=100)
# 将每个点与它的两个最近邻连接
K = 2
for i in range(X.shape[0]):
    for j in nearest_partition[i, :K + 1]:
        # 画一条从X[i]到X[j]的线段
        # 用zip方法实现:
        plt.plot(*zip(X[j], X[i]), color='black')
plt.show()
# 图中每个点和离它最近的两个节点用连线连接。乍一看,你可能会奇怪为什么有些点的连线多于两条,
# 这是因为点A是点B最邻近的两个节点之一,但是并不意味着点B一定是点A的最邻近的两个节点之一。
