#  Copyright (c) 2022. Generated by Gu.
class DLinkNode:
    """双链表结点类"""

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None


class CDLinkList:
    """双链表类"""

    def __init__(self):
        self.dhead = DLinkNode()
        self.dhead.next = self.dhead
        self.dhead.prior = self.dhead

    # 在p后插入s: s.next = p.next; s.next.prior = s; s.prior = p; p.next = s
    # 删除p结点: p.next.prior = p.prior; p.prior.next = p.next

    def __len__(self):
        length = 0
        node = self.dhead
        while node.next != self.dhead:
            length += 1
            node = node.next
        return length

    def create_list_f(self, a):
        """头插法：由数组a整体建立双链表 n n"""
        for i in range(0, len(a)):
            s = DLinkNode(a[i])  # 新建存放a[i]元素的结点s，插入表头
            s.next = self.dhead.next  # 修改s结点的next成员
            if self.dhead.next != self.dhead:  # 修改头结点的非空后继结点的prior
                self.dhead.next.prior = s
            self.dhead.next = s  # 修改头结点的next
            s.prior = self.dhead  # 修改s结点的prior

    def create_list_r(self, a):
        """尾插法：由数组a整体建立双链表 n n"""
        t = self.dhead  # t始终指向尾结点，开始时指向头结点
        for i in range(0, len(a)):
            s = DLinkNode(a[i])
            t.next = s  # 将s结点插入t结点之后
            s.prior = t
            t = s
        t.next = self.dhead  # 将尾结点的next成员置为None
        self.dhead.prior = t

    def geti(self, index):
        """返回序号为i的结点 O(n)"""
        p = self.dhead
        j = -1
        while j < index:
            j += 1
            p = p.next
            if p == self.dhead:
                break
        return p

    def add(self, e):
        """双链表末尾添加元素e O(n)"""
        s = DLinkNode(e)
        p = self.dhead
        while p.next != self.dhead:  # 查找尾结点
            p = p.next
        p.next = s  # 插入
        s.next = self.dhead

    def getsize(self):
        """返回长度 O(n)"""
        p = self.dhead
        cnt = 0
        while p.next != self.dhead:  # 找到尾结点为止
            cnt += 1
            p = p.next
        return cnt

    def __getitem__(self, item):
        """序号item的元素 O(n)"""
        assert item >= 0
        p = self.geti(item)  # 查找序号item的结点p
        assert p != self.dhead
        return p.data

    def __setitem__(self, key, value):
        """设置序号key的元素"""
        assert key >= 0
        p = self.geti(key)
        assert p != self.dhead  # 查找序号key的结点p
        p.data = value

    def get_no(self, e):
        """查找第一个值为e的元素的序号"""
        j = 0
        p = self.dhead.next
        while p != self.dhead and p.data != e:
            j += 1  # 查找元素e
            p = p.next
        if p == self.dhead:
            return -1
        else:
            return j

    def insert(self, i, e):
        """序号i处插入e n"""
        assert i >= 0
        s = DLinkNode(e)
        p = self.geti(i - 1)  # 查找序号i-1的结点p
        assert p != self.dhead
        s.next = p.next
        if p != self.dhead:  # 修改p的非空后继结点的prior属性
            p.next.prior = s
        p.next = s
        s.prior = p

    def delete(self, i):
        """删除序号为i的元素 n"""
        assert i >= 0
        p = self.geti(i)
        assert p != self.dhead
        p.prior.next = p.next  # 修改p前驱节点的next
        if p.next != self.dhead:  # 修改p结点的非空后继结点的prior
            p.next.prior = p.prior

    def display(self):
        """输出单链表"""
        p = self.dhead.next
        while p != self.dhead:
            print(p.data, end=' ')
            p = p.next
        print()

    def comb(self, b):
        """将a循环双链表添加到self后 1"""
        ta = self.dhead.prior
        tb = b.dhead.prior  # ta指向a的尾结点
        ta.next = b.dhead.next  # tb指向b的尾结点
        b.dhead.next.prior = ta  # 尾首相连
        tb.next = self.dhead
        self.dhead.prior = tb
        return self.display()

    def symm(self):
        """判断是否为对称链表"""
        flag = True
        p = self.dhead.next
        q = self.dhead.prior
        while flag:
            if p.data != q.data:
                flag = False
            else:
                if p == q or p == q.prior:  # 前一个对应奇数，后一个偶数
                    break
                q = q.prior
                p = p.next
        return flag


if __name__ == '__main__':
    a1 = CDLinkList()
    a1.create_list_f([1, 2, 3, 4, 5, 6, 7])
    a1.add(8)
    a1.display()
    print(a1.geti(5))
    print(len(a1))
    print(a1[5])
    a1[3] = 10
    a1.insert(8, 50)
    a1.display()
    print(a1.get_no(6))
    a1.delete(0)
    a1.display()
    a2 = CDLinkList()
    a2.create_list_r([1, 2, 3, 3, 2, 1])
    a2.display()
    a1.comb(a2)
    print(a2.symm())
