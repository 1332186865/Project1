from AdjGraph import AdjGraph

MAXV = 100  # 全局变量，表示最多顶点个数
visited = [0] * MAXV  # 全局访问标志数组


# 解法1
def FindallPath1(G, u, v):  # 求u到v的所有简单路径
    path = [-1] * MAXV
    d = -1  # path[0..d]存放一条路径
    for i in range(len(visited)): visited[i] = 0  # 初始化
    FindallPath11(G, u, v, path, d)


def FindallPath11(G, u, v, path, d):  # 被Findapath1调用
    visited[u] = 1
    d += 1
    path[d] = u  # 顶点u加入到路径中
    if u == v:  # 找到一条路径后输出
        for i in range(d + 1):
            print('  ' + str(path[i]), end='')
        print()  # 输出一条路径后返回
        visited[u] = 0  # 回溯,重置visited[u]为0
        return
    for j in range(len(G.adjlist[u])):  # 处理顶点u的所有出边
        w = G.adjlist[u][j].adjvex  # 取顶点u的第j个邻接点w
        if visited[w] == 0:  # w没有访问过
            FindallPath11(G, w, v, path, d)  # 递归调用
    visited[u] = 0  # 回溯,重置visited[u]为0


# 解法2
inpath = [0] * MAXV  # 全局数组


def FindallPath2(G, u, v):  # 求u到v的所有简单路径
    for i in range(len(inpath)): inpath[i] = 0  # 初始化inpath
    path = [u]  # 将顶点u添加的path中
    inpath[u] = 1  # 置u已经在path中
    FindallPath21(G, u, v, path)


def FindallPath21(G, u, v, path):  # 被Findapath函数调用
    if u == v:  # 找到一条路径后输出
        print(' ', path)
        return
    for j in range(len(G.adjlist[u])):  # 处理顶点u的所有出边
        w = G.adjlist[u][j].adjvex  # 取顶点u的第j个邻接点w
        if inpath[w] == 0:  # 若顶点w不在path中
            path.append(w)  # 将顶点w添加的path中
            inpath[w] = 1  # 置w已经在path中
            FindallPath21(G, w, v, path)  # 递归调用
            path.pop()  # path回溯
            inpath[w] = 0  # 置w不在path中


# 主程序
G = AdjGraph()
n, e = 6, 9
a = [[0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], \
     [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
G.CreateAdjGraph(a, n, e)
print("图G")
G.DispAdjGraph()
u, v = 0, 5
print("解法1:%d到%d的所有结点路径:" % (u, v))
FindallPath1(G, u, v)
print("解法2:%d到%d的所有结点路径:" % (u, v))
FindallPath2(G, u, v)
