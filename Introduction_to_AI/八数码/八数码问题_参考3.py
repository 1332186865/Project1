# encoding:utf-8

"""
@ProjectName:AI_Projects
@Author:只想AC
@File:深度优先搜索解八数码问题.py
@Date:2022/4/5
"""

from copy import deepcopy


def judge():
    for i in range(Sum):
        if mat[i] == a and Dep[i] <= depth:  # and Dep[i] <= depth
            return True
    return False


def matched():
    if a == [[1, 2, 3], [8, 0, 4], [7, 6, 5]]:
        return True
    return False


def Out():
    print("总搜索步数：", Sum - 1)  # 减1是减去初始状态那一步
    print("解路径长度：", depth)
    with open('Mat.txt', 'w', encoding='utf-8') as file_object:
        file_object.write("总搜索路径如下：\n")
        for i in range(0, Sum):
            file_object.write("当前步数: " + str(i) + " 当前深度: " + str(Dep[i]) + '\n')
            for j in range(3):
                file_object.write(str(mat[i][j]) + '\n')
            file_object.write('\n')
    with open('Res.txt', 'w', encoding='utf-8') as file_object:
        file_object.write("解路径如下：\n")
        for i in range(0, depth + 1):
            file_object.write("当前深度: " + str(Dep[i]) + '\n')
            for j in range(3):
                file_object.write(str(res[i][j]) + '\n')
            file_object.write('\n')
    return


def dfs(x, y):
    global ft
    global depth
    global dx
    global dy
    global Sum
    if ft is True or depth >= MAX_Depth or Sum > MAX_Sum:  # 已经找到目标状态or当前深度大于等于最大深度or当前搜索总步数超过最大步数则返回
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            depth += 1
            if not judge():
                res.append(deepcopy(a))
                mat.append(deepcopy(a))
                Dep.append(depth)
                Sum += 1
                if matched() is True:
                    Out()
                    ft = True
                    return
                else:
                    dfs(nx, ny)
                    a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                    depth -= 1
                    res.pop()
            else:
                a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                depth -= 1


if __name__ == '__main__':
    # 初始化
    n = 3
    # a = [[2, 3, 1], [5, 0, 8], [4, 6, 7]]  # 八数码矩阵
    # a = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    a = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    # 空格开始的横、纵坐标
    sx = 0
    sy = 0
    MAX_Sum = 50000  # 最大搜索步数
    MAX_Depth = 200  # 最大搜索深度
    ft = False  # 记录是否找到目标状态
    # 空格移动方向下、左、右、上
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    global Sum
    Sum = 1  # 记录总步数
    depth = 0  # 记录深度
    global mat
    mat = [[[]]]  # 记录已经走过的状态
    global res
    res = [[[]]]  # 记录解路径
    global Dep
    Dep = []  # 记录每一个走过的状态的深度
    # print("请输入初始状态：")
    # 输入
    # for i in range(n):
    #     a[i] = list(map(int, input().split(' ')))
    # MAX_Depth = 50
    # 找出初始0的位置，记为(sx,sy)
    for i in range(3):
        for j in range(3):
            if a[i][j] == 0:
                sx = i
                sy = j
    # 存储初始状态表示已走过
    mat.pop()
    res.pop()
    mat.append(deepcopy(a))
    res.append(deepcopy(a))
    Dep.append(0)
    dfs(sx, sy)
    if not ft:
        print("Not Found!")
        Out()

'''
0 1 3
4 2 5
7 8 6
15

1 5 3
2 4 6
7 0 8
5
'''
