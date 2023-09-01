def Height(t):  # 求t的高度
    if len(t) == 1:  # 叶子结点高度为1
        return 1
    m = len(t)
    maxsh = 0
    for i in range(1, m):  # 遍历所有子树
        sh = Height(t[i])  # 求子树t[i]的高度
        maxsh = max(maxsh, sh)  # 求所有子树的最大高度
    return maxsh + 1


t = ['A', ['B', ['D'], ['E', ['G']], ['F']], ['C']]
# t=['A',['B',['E'],['F']],['C',['G',['J']]],['D',['H'],['I',['K'],['L'],['M']]]]
print(Height(t))
