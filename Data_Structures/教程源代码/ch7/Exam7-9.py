from collections import deque

from AdjGraph import AdjGraph

MAXV = 100  # 全局变量，表示最多顶点个数
visited = [0] * MAXV


class QNode:  # 队列元素类
    def __init__(self, p, pre):  # 构造方法
        self.vno = p  # 当前顶点编号
        self.pre = pre  # 当前结点的前驱结点


def ShortPath(G, u, v):  # 求u到v的一条最短简单路径
    res = []  # 存放结果
    qu = deque()  # 定义一个队列qu
    qu.append(QNode(u, None))  # 起始点u(前驱为None)进队
    visited[u] = 1  # 置已访问标记
    while len(qu) > 0:  # 队不空循环
        p = qu.popleft()  # 出队一个结点
        if p.vno == v:  # 当前结点p为v结点
            res.append(v)
            q = p.pre  # q为前驱结点
            while q is not None:  # 找到起始结点为止
                res.append(q.vno)
                q = q.pre
            res.reverse()  # 逆置res构成正向路径
            return res
        for j in range(len(G.adjlist[p.vno])):  # 处理顶点u的所有出边
            w = G.adjlist[p.vno][j].adjvex  # 取顶点u的第j个邻接点w
            if visited[w] == 0:  # w没有访问过
                qu.append(QNode(w, p))  # 置其前驱结点为p
                visited[w] = 1  # 置已访问标记


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
print("    %d->%d最短路径" % (u, v), ShortPath(G, u, v))
