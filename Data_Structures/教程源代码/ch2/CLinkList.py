class LinkNode:  # 循环单链表结点类
    def __init__(self, data=None):  # 构造函数
        self.data = data  # data域
        self.next = None  # next域


class CLinkList:  # 循环单链表类
    def __init__(self):  # 构造函数
        self.head = LinkNode()  # 头结点head
        self.head.next = self.head  # 构成循环的

    def CreateListF(self, a):  # 头插法：由数组a整体建立循环单链表
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i])  # 新建存放a[i]元素的结点s
            s.next = self.head.next  # 将s结点插入到开始结点之前,头结点之后
            self.head.next = s

    def CreateListR(self, a):  # 尾插法：由数组a整体建立循环单链表
        t = self.head  # t始终指向尾结点,开始时指向头结点
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i])  # 新建存放a[i]元素的结点s
            t.next = s  # 将s结点插入t结点之后
            t = s
        t.next = self.head  # 将尾结点的next改为指向头结点

    def geti(self, i):  # 返回序号为i的结
        p = self.head  # 首先p指向头结点
        j = -1
        while j < i:
            j += 1
            p = p.next
            if p == self.head: break
        return p

    def Add(self, e):  # 在线性表的末尾添加一个元素e
        s = LinkNode(e)  # 新建结点s
        p = self.head
        while p.next != self.head:  # 查找尾结点p
            p = p.next
        p.next = s  # 在尾结点之后插入结点s
        s.next = self.head

    def getsize(self):  # 返回长度
        p = self.head
        cnt = 0
        while p.next != self.head:  # 找到尾结点为止
            cnt += 1
            p = p.next
        return cnt

    def __getitem__(self, i):  # 求序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p != self.head  # p不为头结点的检测
        return p.data

    def __setitem__(self, i, x):  # 设置序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p != self.head  # p不为图结点的检测
        p.data = x

    def GetNo(self, e):  # 查找第一个为e的元素的序号
        j = 0
        p = self.head.next  # 首先p指向首结点
        while p != self.head and p.data != e:
            j += 1  # 查找元素e
            p = p.next
        if p == self.head:
            return -1  # 未找到时返回-1
        else:
            return j  # 找到后返回其序号

    def Insert(self, i, e):  # 在线性表中序号i位置插入元素e
        assert i >= 0  # 检测参数i正确性的断言
        s = LinkNode(e)  # 建立新结点s
        if i == 0:  # 插入作为首结点
            s.next = self.head.next
            self.head.next = s
        else:
            p = self.geti(i - 1)  # 找到序号为i-1的结点p
            assert p != self.head  # p不为头结点的检测
            s.next = p.next  # 在p结点后面插入s结点
            p.next = s

    def Delete(self, i):  # 在线性表中删除序号i位置的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i - 1)  # 找到序号为i-1的结点p
        assert p.next != self.head  # p.next不为头结点的检测
        p.next = p.next.next  # 删除p结点的后继结点

    def display(self):  # 输出线性表
        p = self.head.next  # 首先p指向首结点
        while p != self.head:
            print(p.data, end=' ')
            p = p.next
        print()


if __name__ == '__main__':
    L = CLinkList()
    a = [1, 2, 3, 4, 1]
    L.CreateListR(a)
    print("L: ", end=''), L.display()
    i = 0
    x = 10
    print("在序号%d处插入%d" % (i, x))
    L.Insert(i, x)
    print("L: ", end=''), L.display()

    i = 5
    print("删除序号%d处元素" % i)
    L.Delete(i)
    print("L: ", end=''), L.display()

    x = 20
    print("添加%d元素" % x)
    L.Add(x)
    print("L: ", end=''), L.display()

    print("元素1的序号是%d" % (L.GetNo(1)))
    print("L: ", end=''), L.display()
