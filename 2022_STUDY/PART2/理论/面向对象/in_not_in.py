#  Copyright (c) 2022. Generated by Gu.
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r) ' % self.data

    def __contains__(self, item):  # e代表测试元素
        print("__contains__被调用")
        for x in self.data:
            if item == x:
                return True
        return False


L1 = MyList([1, -2, 3, 4, 5])
if 2 in L1:
    print("Yes")
else:
    print("No")
