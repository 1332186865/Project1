#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
from copy import deepcopy


class Solution:
    def __init__(self, matrix_origin: list, matrix_target: list):
        """
        :param matrix_origin: 初始矩阵
        :param matrix_target: 目标矩阵
        """
        # 矩阵
        self.origin = matrix_origin
        self.target = matrix_target
        # (0 ,0)
        self.sx = 0
        self.sy = 0
        # 空格移动方向
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        # 限制条件
        self.max_sum = 30000
        self.max_depth = 50
        # 记录
        self.sum = 1
        self.depth = 0
        self.status = False
        # 状态表
        self.all = []  # 所有路径
        self.open = []  # 解题路径
        self.deep = []  # 每一步所在深度

    def judge(self) -> bool:
        """
        判断以前是否搜寻到结果

        :rtype: bool
        """
        for i in range(self.sum):
            if self.all[i] == self.origin and self.deep[i] <= self.depth:
                return True
        return False

    def matched(self) -> bool:
        """
        判断当前矩阵是否与目标矩阵相符

        :rtype: bool
        """
        if self.target == self.origin:
            return True
        return False

    def save(self):
        """
        将每次搜寻结果与最终结果写入文件
        """
        print("总搜索步数：", self.sum - 1)
        print("解路径长度：", self.depth)
        with open('Ans.txt', 'w', encoding='utf8') as file:
            file.write('解路径如下：\n')
            for i in range(self.depth + 1):
                file.write(f'当前深度: {self.deep[i]}\n')
                for j in range(3):
                    file.write(f'{self.open[i][j]}\n')
                file.write('\n')
        with open('Mat.txt', 'w', encoding='utf8') as file:
            file.write('总路径如下：\n')
            for i in range(self.sum):
                file.write(f'当前步数: {i}, 当前深度: {self.deep[i]}\n')
                for j in range(3):
                    file.write(f'{self.all[i][j]}\n')
                file.write('\n')

    def dfs(self, x: int, y: int):
        """
        深度优先算法

        :param x: 空格所在的横坐标
        :param y: 空格所在的纵坐标
        :return: None
        """
        if self.sum >= self.max_sum or self.status or self.depth >= self.max_depth:
            return
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                self.origin[x][y], self.origin[nx][ny] = self.origin[nx][ny], self.origin[x][y]
                self.depth += 1
                if not self.judge():
                    self.all.append(deepcopy(self.origin))
                    self.open.append(deepcopy(self.origin))
                    self.deep.append(self.depth)
                    self.sum += 1
                    if self.matched():
                        self.save()
                        self.status = True
                        return
                    else:
                        self.dfs(nx, ny)
                        self.origin[nx][ny], self.origin[x][y] = self.origin[x][y], self.origin[nx][ny]
                        self.depth -= 1
                        self.open.pop()
                else:
                    self.origin[nx][ny], self.origin[x][y] = self.origin[x][y], self.origin[nx][ny]
                    self.depth -= 1

    def main(self):
        """主程序"""
        # 找出(0, 0)所在位置
        for i in range(3):
            for j in range(3):
                if self.origin[i][j] == 0:
                    self.sx = i
                    self.sy = j

        self.open.append(deepcopy(self.origin))
        self.all.append(deepcopy(self.origin))
        self.deep.append(0)
        self.dfs(self.sx, self.sy)
        if not self.status:
            print('未找到路径')
            self.save()


if __name__ == '__main__':
    start = [[0, 2, 3], [1, 8, 4], [7, 6, 5]]
    target = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    Solution(start, target).main()
