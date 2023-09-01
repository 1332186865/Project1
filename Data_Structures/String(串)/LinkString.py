class LinkNode:
    """链串结点类型"""
    def __init__(self, d=None):
        self.data = d  # 存放一个字符
        self.next = None  # 指向下一个结点的指针


class LinkString:
    """链串类"""
    def __init__(self):
        self.head = LinkNode()  # 建立头结点
        self.size = 0

    # 串的基本运算算法
    def str_assign(self, cstr):
        """创建一个串"""
        t = self.head  # t始终指向尾结点
        for i in range(len(cstr)):  # 循环建立字符结点
            p = LinkNode(cstr[i])
            t.next = p
            t = p  # 将p结点插入到尾部
            self.size += 1
        t.next = None  # 尾结点的next置为空

    def str_copy(self):
        """串复制"""
        s = LinkString()
        t = s.head  # t始终指向s链串的尾结点
        p = self.head.next
        while p is not None:
            q = LinkNode(p.data)
            t.next = q
            t = q
            p = p.next
        t.next = None  # 尾结点的next置为空
        return s

    def getsize(self):
        """求串长"""
        return self.size

    def __getitem__(self, i):
        """求序号为i的元素"""
        assert 0 <= i < self.size  # 检测参数i正确性的断言
        p = self.head
        j = -1
        while j < i:  # 查找序号为i的结点p
            j += 1
            p = p.next
        return p.data  # 返回p结点值

    def __setitem__(self, i, x):
        """设置序号为i的元素"""
        assert 0 <= i < self.size  # 检测参数
        p = self.head
        j = -1
        while j < i:  # 查找序号为i的结点p
            j += 1
            p = p.next
        p.data = x  # 置p结点值为x

    def concat(self, t):
        """串连接"""
        s = LinkString()  # 新建一个空串
        p = self.head.next
        r = s.head
        while p is not None:  # 将当前链串的所有结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        p = t.head.next
        while p is not None:  # 将链串t的所有结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        s.size = self.size + t.size
        r.next = None  # 尾结点的next置为空
        return s  # 返回新串s

    def sub_str(self, i, j):
        """求子串"""
        s = LinkString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        p = self.head.next
        t = s.head  # t指向新建链表的尾结点
        for k in range(i):  # 移动i-1个结点
            p = p.next
        for k in range(j):  # 将s的序号i结点开始的j个结点复制到s
            q = LinkNode(p.data)
            t.next = q
            t = q  # 将q结点插入到尾部
            p = p.next
        s.size = j
        t.next = None  # 尾结点的next置为空
        return s  # 返回新建的链串

    def ins_str(self, i, t):
        """串插入"""
        s = LinkString()  # 新建一个空串
        assert 0 <= i < self.size  # 检测参数
        p = self.head.next
        p1 = t.head.next
        r = s.head  # r指向新建链表的尾结点
        for k in range(i):  # 将当前链串的前i个结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        while p1 is not None:  # 将t中所有结点复制到s
            q = LinkNode(p1.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p1 = p1.next
        while p is not None:  # 将p及其后的结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        s.size = self.size + t.size
        r.next = None  # 尾结点的next置为空
        return s  # 返回新建的链串

    def del_str(self, i, j):
        """串删除"""
        s = LinkString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        p = self.head.next
        t = s.head  # t指向新建链表的尾结点
        for k in range(i):  # 将s的前i个结点复制到s
            q = LinkNode(p.data)
            t.next = q
            t = q  # 将q结点插入到尾部
            p = p.next
        for k in range(j):  # 让p沿next跳j个结点
            p = p.next
        while p is not None:  # 将p及其后的结点复制到s
            q = LinkNode(p.data)
            t.next = q
            t = q  # 将q结点插入到尾部
            p = p.next
        s.size = self.size - j
        t.next = None  # 尾结点的next置为空
        return s  # 返回新建的链串

    def rep_str(self, i, j, t):
        """串替换"""
        s = LinkString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        p = self.head.next
        p1 = t.head.next
        r = s.head  # r指向新建链表的尾结点
        for k in range(i):  # 将s的前i个结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        for k in range(j):  # 让p沿next跳j个结点
            p = p.next
        while p1 is not None:  # 将t中所有结点复制到s
            q = LinkNode(p1.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p1 = p1.next
        while p is not None:  # 将p及其后的结点复制到s
            q = LinkNode(p.data)
            r.next = q
            r = q  # 将q结点插入到尾部
            p = p.next
        s.size = self.size - j + t.size
        r.next = None  # 尾结点的next置为空
        return s  # 返回新建的链串

    def disp_str(self):
        """输出串"""
        p = self.head.next
        while p is not None:
            print(p.data, end='')
            p = p.next
        print()

    def str_equeal(self, t):
        if self.getsize() != t.getsize():
            return False
        p = self.head.next
        q = t.head.next
        while p is not None and q is not None:
            if p.data != q.data:
                return False
            p = p.next
            q = q.next
        return True


if __name__ == '__main__':
    cstr1 = "abcd"
    cstr2 = "123"
    s1 = LinkString()
    s1.str_assign(cstr1)
    print("s1: ", end='')
    s1.disp_str()
    print("s1的长度: %d" % (s1.getsize()))
    s2 = LinkString()
    s2.str_assign(cstr2)
    print("s2: ", end='')
    s2.disp_str()
    print("s2的长度: %d" % (s2.getsize()))
    print("s1=>s3")
    s3 = s1.str_copy()
    print("s3: ", end='')
    s3.disp_str()
    print("s1和s2连接=>s4")
    s4 = s1.concat(s2)
    print("s4: ", end='')
    s4.disp_str()
    print("s4[2..5]=>s5")
    s5 = s4.sub_str(2, 5)
    print("s5: ", end='')
    s5.disp_str()
    print("s4中序号2位置插入s2=>s6")
    s6 = s4.ins_str(2, s2)
    print("s6: ", end='')
    s6.disp_str()
    print("s6中删除[2,3]=>s7")
    s7 = s6.del_str(2, 3)
    print("s7: ", end='')
    s7.disp_str()
    print("s6中[2,3]替换为s1=>s8")
    s8 = s6.rep_str(2, 3, s1)
    print("s8: ", end='')
    s8.disp_str()
