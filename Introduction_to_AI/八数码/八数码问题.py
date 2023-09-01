#  -*- coding=utf-8 -*-
from copy import deepcopy


class Solution:
    def __init__(self, matrix_origin: list, matrix_target: list):
        """
        :param matrix_origin: 初始矩阵
        :param matrix_target: 目标矩阵
        """
        self.origin = matrix_origin
        self.target = matrix_target
        self.status = False  # 记录是否找到目标状态

        # 空格开始的横、纵坐标
        self.sx = 0
        self.sy = 0

        # 空格移动方向下、左、右、上
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]

        self.MAX_Sum = 30000  # 最大搜索步数
        self.MAX_Depth = 50  # 最大搜索深度

        self.Sum = 1  # 记录总步数
        self.depth = 0  # 记录深度

        self.Dep = []  # 记录每一个走过的状态的深度

        self.mat = [[]]  # 记录已经走过的状态
        self.res = [[]]  # 记录解路径

    def judge(self) -> bool:
        """
        判断是否搜寻到结果

        :rtype: bool
        """
        for i in range(self.Sum):
            if self.mat[i] == self.origin and self.Dep[i] <= self.depth:
                return True
        return False

    def matched(self) -> bool:
        """
        判断当前矩阵是否与目标矩阵相符

        :rtype: bool
        """
        if self.origin == self.target:
            return True
        return False

    def search(self):
        """
        将每次搜寻结果与最终结果写入文件
        """
        print("总搜索步数：", self.Sum - 1)
        print("解路径长度：", self.depth)
        with open('Mature.txt', 'w', encoding='utf-8') as file:  # 记录全部尝试
            file.write("总搜索路径如下：\n")
            for i in range(0, self.Sum):
                file.write("当前步数: " + str(i) + " 当前深度: " + str(self.Dep[i]) + '\n')
                for j in range(3):
                    file.write(str(self.mat[i][j]) + '\n')
                file.write('\n')
        with open('Answer.txt', 'w', encoding='utf-8') as file:  # 记录正确搜索路径
            file.write("解路径如下：\n")
            for i in range(0, self.depth + 1):
                file.write("当前深度: " + str(self.Dep[i]) + '\n')
                for j in range(3):
                    file.write(str(self.res[i][j]) + '\n')
                file.write('\n')
        return

    def dfs(self, x: int, y: int):
        """
        深度优先算法

        :param x: 空格所在的横坐标
        :param y: 空格所在的纵坐标
        :return: None
        """
        if self.status or self.depth >= self.MAX_Depth or self.Sum > self.MAX_Sum:
            # 已经找到目标状态 or 当前深度大于等于最大深度 or 当前搜索总步数超过最大步数则返回
            return
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                self.origin[x][y], self.origin[nx][ny] = self.origin[nx][ny], self.origin[x][y]
                self.depth += 1
                if not self.judge():
                    self.res.append(deepcopy(self.origin))
                    self.mat.append(deepcopy(self.origin))
                    self.Dep.append(self.depth)
                    self.Sum += 1
                    if self.matched():
                        self.search()
                        self.status = True
                        return
                    else:
                        self.dfs(nx, ny)
                        self.origin[nx][ny], self.origin[x][y] = self.origin[x][y], self.origin[nx][ny]
                        self.depth -= 1
                        self.res.pop()
                else:
                    self.origin[nx][ny], self.origin[x][y] = self.origin[x][y], self.origin[nx][ny]
                    self.depth -= 1

    def main(self):
        """主程序"""
        # 找出初始0的位置，记为(sx,sy)
        for i in range(3):
            for j in range(3):
                if self.origin[i][j] == 0:
                    self.sx = i
                    self.sy = j

        # 存储初始状态表示已走过
        self.mat.pop()
        self.res.pop()
        self.mat.append(deepcopy(self.origin))
        self.res.append(deepcopy(self.origin))
        self.Dep.append(0)
        self.dfs(self.sx, self.sy)
        if not self.status:
            print("目前未发现路径!")
            self.search()


if __name__ == '__main__':
    start = [[0, 2, 3], [1, 8, 4], [7, 6, 5]]
    target = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    Solution(start, target).main()
