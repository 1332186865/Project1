from LinkList import LinkList


def geti(key, r, i):  # 求基数为r的正整数key的第i位
    k = 0
    for j in range(i + 1):
        k = key % r
        key = key // r
    return k


def RadixSort(L, d, r):  # 最低位优先基数排序算法
    # t=None
    front = [None] * r  # 建立链队队头数组
    rear = [None] * r  # 建立链队队尾数组
    for i in range(d):  # 从低位到高位循环
        for j in range(r):  # 初始化各链队首、尾指针
            front[j] = rear[j] = None
        p = L.head.next  # p指向单链表L的首结点
        while p is not None:  # 分配：对于原链表中每个结点循环
            k = geti(p.data, r, i)  # 提取结点关键字的第i个位k
            if front[k] is None:  # 第k个链队空时,队头队尾均指向p结点
                front[k] = p
                rear[k] = p
            else:  # 第k个链队非空时,p结点进队
                rear[k].next = p
                rear[k] = p
            p = p.next  # 取下一个结点
        t = L.head  # 重新用h来收集所有结点
        for j in range(r):  # 收集：对于每一个链队循环
            if front[j] is not None:  # 若第j个链队是第一个非空链队
                t.next = front[j]
                t = rear[j]
        t.next = None  # 尾结点的next置空
        print("第%d趟排序的结果:" % i, end=' ')
        L.display()
    return L


L = LinkList()
a = [75, 23, 98, 44, 57, 12, 29, 64, 38, 82]
L.CreateListR(a)
print("L: ", end=''), L.display()
print("排序")
r = 10
d = 2
L = RadixSort(L, d, r)
print("L: ", end=''), L.display()
