# 有一个死胡同，宽度刚好只能让一辆汽车通过，偏偏老有汽车开到死胡同来，这下麻烦了，最先开来的汽车要最后才能倒退出去。给定一个汽车开来的序列和一个可能的倒车出去的序列，
# 请判断汽车能否都倒退出去，若能则输出Yes，否则输出No。
# 首先输入一个整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据首先输入一个正整数n（n≤10），代表开来的汽车数，然后输入2n个整数，
# 其中，前n个整数表示汽车开来的序列，后n个整数表示汽车可能倒出的序列。
# 对于每组测试，判断能否倒车出该死胡同，若能则输出“Yes”，否则输出“No”。引号不必输出。
# 2
# 4 1 2 3 4 2 1 4 3
# 4 1 2 3 4 4 2 1 3
# Yes
# No
class Sqstack:
    def __init__(self):
        self.data = []

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 进栈
        self.data.append(e)

    def pop(self):  # 出栈
        assert not self.empty()
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.data[-1]


def isTrue(ls1, ls2, n):  # 列表1，列表2，列表长度
    sq = Sqstack()
    cnt = 0
    for i in range(n):
        sq.push(ls1[i])  # 进栈
        while not sq.empty() and (sq.gettop() == ls2[cnt]):  # 取栈顶与第二个列表各项进行比较
            sq.pop()  # 出栈
            cnt += 1
    return sq.empty()  # 若空，返回TRUE


a = int(input())
for _ in range(a):
    b = input().split(' ')  # 将输入分成三部分，后两部分变成列表
    lis1 = [int(b[i + 1]) for i in range(int(b[0]))]
    lis2 = [int(b[int(b[0]) + i + 1]) for i in range(int(b[0]))]
    print(lis1, lis2)
    if isTrue(lis1, lis2, int(b[0])):
        print('Yes')
    else:
        print('No')
