# 设某银行有A、B两个业务窗口，且处理业务的速度不一样，其中A窗口处理速度是B窗口的2倍 —— 即当A窗口每处理完2个顾客时，B窗口处理完1个顾客。给定到达银行的顾客序列，请按业务完成的顺序输出顾客序列。假定不考虑顾客先后到达的时间间隔，并且当不同窗口同时处理完2个顾客时，A窗口顾客优先输出。
# 输入格式:输入为一行正整数，其中第1个数字N(≤1000)为顾客总数，后面跟着N位顾客的编号。编号为奇数的顾客需要到A窗口办理业务，为偶数的顾客则去B窗口。数字间以空格分隔。
# 输出格式:按业务处理完成的顺序输出顾客的编号。数字间以空格分隔，但最后一个编号后不能有多余的空格。
# 输入样例:
# 8 2 1 3 9 4 11 13 15
# 结尾无空行
# 输出样例:
# 1 3 2 9 11 4 13 15
MaxSize = 100


# 存在错误

class SqQueue:  # 非循环队列类
    def __init__(self):
        self.data = [None] * MaxSize  # 存放队列元素
        self.front = -1  # 队头指针
        self.rear = -1  # 队尾指针

    def empty(self):
        return self.front == self.rear

    def push(self, e):  # 队尾插入，改变队尾指针
        assert not self.rear == MaxSize - 1
        self.rear += 1
        self.data[self.rear] = e

    def pop(self):  # 队头删除，改变队头指针
        assert not self.empty()
        self.front += 1
        return self.data[self.front]

    def gethead(self):  # 取队头元素
        assert not self.empty()
        return self.data[self.front + 1]


def solution(n, ls):
    sq1 = SqQueue()
    sq2 = SqQueue()
    for i in range(n):
        if ls[i] % 2 == 1:
            sq1.push(ls[i])
        else:
            sq2.push(ls[i])
    m = 0
    while not sq1.empty() and not sq2.empty():
        if m == 0:
            print(sq1.gethead(), end='')
            sq1.pop()
            m += 1
            print(' ', end='')
            print(sq1.gethead(), end='')
            sq1.pop()
        else:
            print(' ', end='')
            print(sq1.gethead(), end='')
            sq1.pop()
            m += 1
            print(' ', end='')
            print(sq1.gethead(), end='')
            sq1.pop()
        if not sq2.empty():
            print(' ', end='')
            print(sq2.gethead(), end='')
            sq2.pop()
    while not sq1.empty() and sq2.empty():
        if m == 0:
            print(sq1.gethead(), end='')
            sq1.pop()
            m += 1
        else:
            print(' ', end='')
            print(sq1.gethead(), end='')
            sq1.pop()
            m += 1
    while sq1.empty() and not sq2.empty():
        if m == 0:
            print(sq2.gethead(), end='')
            sq2.pop()
            m += 1
        else:
            print(' ', end='')
            print(sq2.gethead(), end='')
            sq2.pop()
            m += 1
    return 0


lis = [int(i) for i in input().split(' ')]
n = lis.pop(0)
solution(n, lis)
