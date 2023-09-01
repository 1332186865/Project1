from AdjGraph import AdjGraph

MAXV = 100  # 全局变量，表示最多顶点个数
visited = [0] * MAXV  # 全局访问标志数组


def HasPath(G, u, v):  # 判断u到v是否有简单路径
    for i in range(len(visited)): visited[i] = 0  # 初始化
    return HasPath1(G, u, v)


def HasPath1(G, u, v):  # 被HasPath方法调用
    visited[u] = 1
    for j in range(len(G.adjlist[u])):  # 处理顶点u的所有出边顶点
        w = G.adjlist[u][j].adjvex  # 取顶点u的一个邻接点w
        if w == v:  # 找到目标点后返回真
            return True  # 表示u到v有路径
        if visited[w] == 0:
            if HasPath1(G, w, v) == True: return True
    return False


# 主程序
G = AdjGraph()
n, e = 6, 9
a = [[0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], \
     [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
G.CreateAdjGraph(a, n, e)
print("图G")
G.DispAdjGraph()
u, v = 0, 5
print("求解结果")
print("  顶点%d到顶点%d路径: " % (u, v), end='')
print("有" if HasPath(G, u, v) else "没有")
u, v = 0, 2
print("  顶点%d到顶点%d路径: " % (u, v), end='')
print("有" if HasPath(G, u, v) else "没有")
