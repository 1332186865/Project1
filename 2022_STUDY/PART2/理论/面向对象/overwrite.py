#  Copyright (c) 2022. Generated by Gu.
class MyNumber(object):
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print("__str__方法被调用")
        return "number: %d" % self.data

    def __repr__(self):
        print("__repr__方法被调用")
        return "number: %d" % self.data


n1 = MyNumber(100)
print(str(n1))
print(n1)
print(repr(n1))
