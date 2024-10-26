#  Copyright (c) 2022. Generated by Gu.
# 写一个实现选代器协议的类Primes, 让此类可以生成从b开始的n个素数
class Primes:
    def __init__(self, b, n):
        self.begin = b
        self.count = n

    @staticmethod
    def __isprime(j):
        for i in range(2, j):
            if j % i == 0:
                return False
        return True

    def __iter__(self):
        self.cur_pos = self.begin  # 迭代起始值
        self.cur_count = 0  # 记录生成数量
        return self

    def __next__(self):
        # 已完成生成,不需要再生成,我停止迭代
        if self.cur_count >= self.count:
            raise StopIteration
        self.cur_count += 1
        while True:
            if self.__isprime(self.cur_pos):
                v = self.cur_pos
                self.cur_pos += 1
                return v
            self.cur_pos += 1


for x in Primes(10, 4):
    print(x)  # 11 13 17 19
