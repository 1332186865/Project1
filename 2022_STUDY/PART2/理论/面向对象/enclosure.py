#  Copyright (c) 2022. Generated by Gu.
class A:
    def __init__(self):
        self.__pi = 100  # 创建私有属性

    def test(self):
        print(self.__pi)


a = A()
# print(a.__pi) 无效
