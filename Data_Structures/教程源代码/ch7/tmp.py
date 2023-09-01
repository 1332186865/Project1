# 解法1
def solve1():
    global n, visited
    ans = []
    for i in range(1, n + 1):
        if visited[i] == 0:
            cnt = DFS(G, i)
            if cnt > 1: ans.append(cnt)
    ans.sort()
    return ans


def DFS(G, v):  # 邻接表G中从顶点v出发的深度优先遍历
    global visited
    cnt = 1  # 访问顶点v
    visited[v] = 1  # 置已访问标记
    if G[v] is None: return cnt
    for j in range(len(G[v])):  # 处理顶点v的所有出边顶点j
        w = G[v][j]  # 取顶点v的一个相邻点w
        if visited[w] == 0:
            cnt += DFS(G, w)  # 若w顶点未访问,递归访问它
    return cnt


# 主程序
n, m = map(int, input().split())  # 转换为整数序列
G = [None] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    if G[a] is None: G[a] = []
    if G[b] is None: G[b] = []
    G[a].append(b)
    G[b].append(a)
print(G)
visited = [0] * (n + 1)
ans = solve1()
print("共有%d个朋友圈" % (len(ans)))
print("各朋友圈人数:", ans)
