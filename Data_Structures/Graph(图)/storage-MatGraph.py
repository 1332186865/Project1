#  Copyright (c) 2022. Generated by Gu.
import copy

INF = 0x3f3f3f3f


class MatGraph:  # ? O(n^2)
    """图邻接矩阵类"""

    def __init__(self, n=0, e=0):
        self.edges = []  # 邻接矩阵数组
        self.vexs = []  # vexs[i]存放顶点i的信息，暂时未用
        self.n = n  # 顶点数
        self.e = e  # 边数

    def create_mat_graph(self, a, n, e):
        """通过数组a，顶点n与边数e建立的图的邻接矩阵"""
        self.n = n
        self.e = e
        self.edges = copy.deepcopy(a)

    def disp_mat_graphs(self):
        """输出图的邻接矩阵数组"""
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j] == INF:
                    print("%5s" % "∞", end=' ')
                else:
                    print("%5d" % (self.edges[i][j]), end=' ')
            print()

    def degree1(self, v):
        """在无向图邻接矩阵中求顶点v的度"""
        d = 0
        for j in range(self.n):  # 统计第v行的非0非无穷大元素的个数
            if self.edges[v][j] != 0 and self.edges[v][j] != INF:
                d += 1
        return d

    def degree2(self, v):
        """在有向图邻接矩阵中求顶点v的出度与入度"""
        ans = [0, 0]  # 0累计出度， 1累计入度
        for j in range(self.n):
            if self.edges[v][j] != 0 and self.edges[v][j] != INF:  # 统计第v行的非0非无穷大元素的个数为出度
                ans[0] += 1
            if self.edges[v][j] != 0 and self.edges[v][j] != INF:  # 统计第v行的非0非无穷大元素的个数为入度
                ans[1] += 1
        return ans  # 返回出度与入度


# mat = [
#     [0, 1, 0, 1, 1],
#     [1, 0, 1, 1, 0],
#     [0, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 0, 1, 1, 0]
#     ]
mat = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
    ]
mat1 = MatGraph()
mat1.create_mat_graph(mat, 6, 7)
mat1.disp_mat_graphs()
