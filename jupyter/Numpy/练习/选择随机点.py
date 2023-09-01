#  Copyright (c) 2022. Generated by Gu.
# 花哨的索引的一个常见用途是从一个矩阵中选择行的子集。例如我们有一个NxD的矩阵,
# 表示在D个维度的N个点。以下是一个二维正态分布的点组成的数组:
import matplotlib.pyplot as plt
import numpy
import seaborn

seaborn.set()  # 设置绘图风格

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = numpy.random.multivariate_normal(mean, cov, 100)
plt.scatter(X[:, 0], X[:, 1])
plt.show()
indices = numpy.random.choice(X.shape[0], 20, replace=False)
selection = X[indices]
# selection.shape
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', edgecolor='b', s=200)
plt.show()
