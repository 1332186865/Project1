#  Copyright (c) 2022. Generated by Gu.
# 练习:实现两个自定义表的相加
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __add__(self, other):
        print("__add__")
        obj = MyList(self.data + other.data)
        return obj

    def __iadd__(self, other):
        print('__iadd__')
        # obj = MyList(self.data + other.data)
        # return obj  # id不同
        self.data.extend(other.data)  # id相同
        return self

    def __mul__(self, other):
        print('__mul__')
        obj = MyList(self.data * other)
        return obj

    def __rmul__(self, other):
        print('__rmul__')
        obj = MyList(self.data * other)
        return obj

    def __repr__(self):
        return '%r' % repr(self.data)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2
print("L3 = ", L3)  # MyList([1,2,3,4,5,6])
L4 = L1 * 2  # 实现乘法运算
print("L4 = ", L4)  # MyList( [1,2,3,1,2,31)
L5 = 2 * L1
print("L5 = ", L5)
L3 += L1
print("L3 = ", L3)
