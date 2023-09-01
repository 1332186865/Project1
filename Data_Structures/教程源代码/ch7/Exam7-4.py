from AdjGraph import AdjGraph

MAXV = 100  # 全局变量，表示最多顶点个数
visited = [0] * MAXV


def DFS1(G, v):  # 邻接表G中从顶点v出发的深度优先遍历
    visited[v] = 1  # 置已访问标记
    for j in range(len(G.adjlist[v])):  # 处理顶点v的所有出边顶点j
        w = G.adjlist[v][j].adjvex  # 取顶点v的一个邻接点w
        if visited[w] == 0:
            DFS1(G, w)  # 若w顶点未访问,递归访问它


def Connect(G):  # 判断无向图G的连通性
    flag = True
    DFS1(G, 0)  # 调用DSF1算法,从0出发深度优先遍历
    for i in range(G.n):
        if visited[i] == 0:
            flag = False  # 存在没有访问的顶点，则不连通
            break
    return flag


# 主程序
G1 = AdjGraph()
n, e = 5, 8
a = [[0, 1, 0, 1, 1], [1, 0, 1, 1, 0], [0, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 1, 0]]
G1.CreateAdjGraph(a, n, e)
print("图G1")
G1.DispAdjGraph()
print("图G1的连通性: %d" % (Connect(G1)))

visited = [0] * MAXV
G2 = AdjGraph()
n, e = 5, 3
b = [[0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]]
G2.CreateAdjGraph(b, n, e)
print("图G2")
G2.DispAdjGraph()
print("图G2的连通性: %d" % (Connect(G2)))
