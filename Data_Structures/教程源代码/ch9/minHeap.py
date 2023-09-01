from Heap import Heap


class MinHeap(Heap):  # 创建小根堆类
    def cmp(self, x, y):  # 比较方法(小根堆)
        return x > y


# 主程序
if __name__ == '__main__':
    heapq = MinHeap()
    a = [5, 4, 3, 2, 1]
    for i in range(len(a)):
        heapq.append(a[i])
    print("初始序列", end=' ')
    print(a)
    print("排序")
    print("排序序列", end=' ')
    while not heapq.empty():
        print(heapq.pop(), end=' ')
