#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
class Sort:
    def __init__(self, lst=None):
        if lst is None:
            lst = [9, 1, 2, 6, 7, 3, 4, 8]
        self.list = lst

    def bubble(self):
        """冒泡排序"""
        # 外层循环表示比较多少轮
        for i in range(len(self.list) - 1):
            # 内层循环表示每轮比较的次数
            for j in range(len(self.list) - i - 1):
                # 前一个数比后一个数大则交换位置
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
        print(self.list)

    def select(self):
        """选择排序"""
        # 比较多少轮
        for i in range(len(self.list) - 1):
            min_index = i  # 假定i号位置数字最小
            for j in range(i + 1, len(self.list)):
                if self.list[min_index] > self.list[j]:
                    min_index = j
            if i != min_index:
                self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
        print(self.list)

    def insert(self):
        """插入排序"""
        for i in range(1, len(self.list)):
            x = self.list[i]
            j = i
            while j > 0 and self.list[j - 1] > x:
                self.list[j] = self.list[j - 1]
                j -= 1
            self.list[j] = x
        print(self.list)

    def sub_sort(self, low, high):
        """一轮交换"""
        key = self.list[low]
        while low < high:
            while low < high and self.list[high] >= key:
                high -= 1
            self.list[low] = self.list[high]
            while low < high and self.list[low] < key:
                low += 1
            self.list[high] = self.list[low]
        self.list[low] = key
        return low

    def quick(self, low: int, high: int):
        """快速排序

        :param low: 开头元素索引
        :param high: 末尾元素索引
        """
        if low < high:
            key = self.sub_sort(low, high)
            self.quick(low, key - 1)
            self.quick(key + 1, high)


if __name__ == '__main__':
    R = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Sort().bubble()
    Sort().select()
    Sort().insert()
    Sort(R).quick(0, len(R) - 1)
    print(R)
