# 给定一个初始为空的队（队空间长度为10）和一系列进队、出队操作，请编写程序输出经过这些操作后队中的元素。队中元素值均为整数。（采用循环队列完成，禁用一个空间方法）
# 输入格式:输入第1行为1个正整数n，表示操作个数；第2行为给出的n个整数，非0元素表示进队，且此非0值即为进队元素，0元素表示出队。
# 输出格式:
# 第一行按出队顺序输出所有出队元素，以一个空格隔开；如果队空时做出队操作会输出"EMPTY"，如果队满时做进队操作会输出"FULL"。第二行中输出队中所有元素，以一个空格隔开。
# 末尾均有一个空格。
# 输入样例:
# 12
# 3 1 2 0 0 -1 0 0 0 4 5 0
# 结尾无空行
# 输出样例:
# 3 1 2 -1 EMPTY 4
# 5

MaxSize = 10


# 存在部分错误

class CSqQueue:
    def __init__(self):
        self.data = [None] * MaxSize  # 存放队列元素
        self.front = 0  # 队头指针
        self.rear = 0  # 队尾指针
        self.count = 0

    def empty(self):
        return self.front == self.rear

    def full(self):
        return self.count == MaxSize

    def push(self, e):  # 队尾插入，队尾指针rear循环+1
        assert self.count != MaxSize
        self.rear = (self.rear + 1) % MaxSize
        self.data[self.rear] = e
        self.count += 1

    def pop(self):  # 队头删除，队头指针front+1
        assert not self.empty()
        self.count -= 1
        self.front = (self.front + 1) % MaxSize
        return self.data[self.front]

    def gethead(self):  # 取队头元素
        assert not self.empty()
        head = (self.front + 1) % MaxSize
        return self.data[head]

    def size(self):
        return (self.rear - self.front + MaxSize) % MaxSize

    def all(self):
        ls = []
        for i in range(self.size()):
            ls.append(CSqQueue.gethead(self))
            CSqQueue.pop(self)
        ls = map(str, ls)
        print(' '.join(ls), end=' ')
        return ' '


def solution(n, lst):
    sq = CSqQueue()
    for i in range(n):
        if lst[i] != 0:
            if not sq.full():
                sq.push(lst[i])
            else:
                print("FULL", end=' ')
        else:
            if not sq.empty():
                print(sq.gethead(), end=' ')
                sq.pop()
            else:
                print("EMPTY", end=' ')
    print()
    return sq.all()


a = int(input())
ls = [int(i) for i in input().split(' ')]
print(solution(a, ls))
