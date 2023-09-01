MaxSize = 100


class SqQueue:
    """非循环队列类(先进先出表)"""

    def __init__(self):
        self.data = [None] * MaxSize  # 存放队列元素
        self.front = -1  # 队头指针
        self.rear = -1  # 队尾指针

    def empty(self):
        return self.front == self.rear

    def push(self, e):
        """队尾插入rear，改变队尾指针"""
        assert not self.rear == MaxSize - 1
        self.rear += 1
        self.data[self.rear] = e

    def pop(self):
        """队头删除front，改变队头指针"""
        assert not self.empty()
        self.front += 1
        return self.data[self.front]

    def gethead(self):
        """取队头元素"""
        assert not self.empty()
        return self.data[self.front + 1]


class CSqQueue:
    """循环队列"""

    def __init__(self):
        self.data = [None] * MaxSize  # 存放队列元素
        self.front = 0  # 队头指针
        self.rear = 0  # 队尾指针
        self.count = 0

    def empty(self):
        return self.count == 0
        # return self.front == self.rear

    def full(self):
        return self.count == MaxSize

    def push(self, e):
        """队尾插入，队尾指针rear循环+1"""
        # assert (self.rear + 1) % MaxSize != self.front
        self.rear = (self.rear + 1) % MaxSize
        # self.data[self.rear] = e
        rear1 = (self.front + self.count) % MaxSize
        assert self.count != MaxSize  # 检测队满
        rear1 = (rear1 + 1) % MaxSize
        self.data[rear1] = e
        self.count += 1  # 元素个数增1

    def pop(self):
        """队头删除，队头指针front+1"""
        assert not self.empty()
        self.front = (self.front + 1) % MaxSize
        self.count -= 1
        return self.data[self.front]

    def gethead(self):
        """取队头元素"""
        assert not self.empty()
        head = (self.front + 1) % MaxSize
        return self.data[head]

    def size(self):
        """返回元素个数"""
        return (self.rear - self.front + MaxSize) % MaxSize

    def push_k(self, k, e):
        """进队第k个元素e"""
        n = self.size()
        if k < 1 or k > n + 1:
            return False
        if k <= n:
            for i in range(1, n + 1):  # 循环处理队中所有元素
                if i == k:
                    self.push(e)  # 将e元素进队到第k个位置
                x = self.pop()
                self.push(x)
        else:
            self.push(e)  # k=n+1时直接进队e
        return True

    def pop_k(self, k):
        """出队第k个元素"""
        n = self.size()
        assert 1 <= k <= n  # 检测参数k错误
        for i in range(1, n + 1):  # 循环处理队中所有元素
            x = self.pop()  # 出队元素x
            if i != k:
                self.push(x)  # 将非第k个元素进队
            else:
                e = x  # 取第k个出队的元素
        return e


if __name__ == '__main__':
    qu = CSqQueue()
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    print("元素个数=%d" % (qu.size()))
    qu.push_k(1, 5)
    qu.pop_k(2)
    while not qu.empty():
        print(qu.pop(), end=' ')
    print()
