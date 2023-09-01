from AdjGraph import AdjGraph

MAXV = 100  # 全局变量，表示最多顶点个数
visited = [0] * MAXV  # 全局访问标志数组


# 解法1
def FindaPath1(G, u, v):  # 求u到v的一条简单路径
    path = [-1] * MAXV
    d = -1  # path[0..d]存放一条路径
    for i in range(len(visited)): visited[i] = 0  # 初始化
    FindaPath11(G, u, v, path, d)


def FindaPath11(G, u, v, path, d):  # 被Findapath1调用
    visited[u] = 1
    d += 1
    path[d] = u  # 顶点u加入到路径中
    if u == v:  # 找到一条路径后输出并返回
        for i in range(d + 1):
            print(path[i], end=' ')
        print()
        return
    for j in range(len(G.adjlist[u])):  # 处理顶点u的所有出边
        w = G.adjlist[u][j].adjvex  # 取顶点u的第j个邻接点w
        if visited[w] == 0:  # w没有访问过
            FindaPath11(G, w, v, path, d)  # 递归调用


# 解法2
def FindaPath2(G, u, v):  # 求u到v的一条简单路径
    path = []
    for i in range(len(visited)): visited[i] = 0  # 初始化
    FindaPath21(G, u, v, path)


def FindaPath21(G, u, v, path):  # 被Findapath2调用
    visited[u] = 1
    path.append(u)  # 顶点u加入到路径中
    if u == v:  # 找到一条路径后输出并返回
        print(path)
        return
    for j in range(len(G.adjlist[u])):  # 处理顶点u的所有出边
        w = G.adjlist[u][j].adjvex  # 取顶点u的第j个邻接点w
        if visited[w] == 0:  # w没有访问过
            FindaPath21(G, w, v, path)  # 递归调用
    path.pop()  # 增加的具有回退功能的代码


# 主程序
G = AdjGraph()
n, e = 6, 9
a = [[0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], \
     [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
G.CreateAdjGraph(a, n, e)
print("图G")
G.DispAdjGraph()
u, v = 0, 4
print("求解结果")
print("  解法1：顶点%d到%d的一条路径:" % (u, v), end='')
FindaPath1(G, u, v)
print("  解法2：顶点%d到%d的一条路径:" % (u, v), end='')
FindaPath2(G, u, v)
