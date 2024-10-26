#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-

import copy


class Set:
    """集合类"""
    MaxSize = 100  # 最多元素个数

    def __init__(self):
        self.data = [None] * Set.MaxSize  # 存放集合元素
        self.size = 0

    def getsize(self):
        """返回集合长度"""
        return self.size

    def get(self, i):
        """返回第i个元素"""
        assert 0 <= i < self.size
        return self.data[i]

    def isin(self, e):
        """判断e是否在集合中"""
        for i in range(self.size):
            if self.data[i] == e:
                return True
        return False

    def add(self, e):
        """添加e"""
        if not self.isin(e):
            self.data[self.size] = e
            self.size += 1

    def delete(self, e):
        """删除e"""
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1
        if i >= self.size:
            return
        for j in range(i + 1, self.size):  # 找到后通过移动实现删除
            self.data[j - 1] = self.data[j]
        self.size -= 1

    def copy(self):
        s1 = Set()
        s1.data = copy.deepcopy(self.data)  # 深复制
        s1.size = self.size
        return s1

    def display(self):
        """输出集合元素"""
        for i in range(self.size):
            print(self.data, end='')
        print()

    def union(self, s2):
        """并集"""
        s3 = self.copy()
        for i in range(s2.getsize()):
            e = s2.get(i)
            if not self.isin(e):
                s3.add(e)
        return s3

    def inter(self, s2):
        """交集"""
        s3 = Set()
        for i in range(self.size):
            e = self.data[i]
            if s2.isin(e):
                s3.add(e)
        return s3

    def diff(self, s2):
        """s1-s2"""
        s3 = Set()
        for i in range(self.size):
            e = self.data[i]
            if not s2.isin(e):
                s3.add(e)
        return s3
