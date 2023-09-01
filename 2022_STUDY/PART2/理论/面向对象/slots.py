#  Copyright (c) 2022. Generated by Gu.
class Student:
    # 限定此类创建的对象只能有这两个属性
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name = n
        self.age = a


s1 = Student('小明', 20)
# s1.Age = 21
# 大小写错误，会报错
