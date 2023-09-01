MaxSize = 100  # 假设容量为100


class SqString:
    """顺序串类"""
    def __init__(self):  # 构造方法
        self.data = [None] * MaxSize  # 存放串中字符
        self.size = 0  # 串中字符个数

    # 串的基本运算算法
    def str_assign(self, cstr):
        """创建一个串"""
        for i in range(len(cstr)):
            self.data[i] = cstr[i]
        self.size = len(cstr)

    def str_copy(self):
        """串复制"""
        s = SqString()
        for i in range(self.size):
            s.data[i] = self.data[i]
        s.size = self.size
        return s

    def getsize(self):
        """求串长"""
        return self.size

    def __getitem__(self, i):
        """求序号为i的元素"""
        assert 0 <= i < self.size  # 检测参数i正确性的断言
        return self.data[i]

    def __setitem__(self, i, x):
        """设置序号为i的元素"""
        assert 0 <= i < self.size  # 检测参数
        self.data[i] = x

    def concat(self, t):
        """串连接"""
        s = SqString()  # 新建一个空串
        s.size = self.size + t.getsize()
        for i in range(self.size):  # 将当前串data[0..str.size-1]->s
            s.data[i] = self.data[i]
        for i in range(t.getsize()):  # 将t.data[0..t.size-1]->s
            s.data[self.size + i] = t.data[i]
        return s  # 返回新串s

    def sub_str(self, i, j):
        """求子串"""
        s = SqString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        for k in range(i, i + j):  # 将data[i..i+j-1]->s
            s.data[k - i] = self.data[k]
        s.size = j
        return s  # 返回新建的顺序串

    def ins_str(self, i, t):
        """串插入"""
        s = SqString()  # 新建一个空串
        assert 0 <= i < self.size  # 检测参数
        for j in range(i):  # 将当前串data[0..i-1]->s
            s.data[j] = self.data[j]
        for j in range(t.getsize()):  # 将t.data[0..t.size-1]->s
            s.data[i + j] = t.data[j]
        for j in range(i, self.size):  # 将当前串data[i..size-1]->s
            s.data[t.size + j] = self.data[j]
        s.size = self.size + t.getsize()
        return s  # 返回新建的顺序串

    def del_str(self, i, j):
        """串删除"""
        s = SqString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        for k in range(i):  # 将当前串data[0..i-1]->s
            s.data[k] = self.data[k]
        for k in range(i + j, self.size):  # 将当前串data[i+j..size-1]->s
            s.data[k - j] = self.data[k]
        s.size = self.size - j
        return s  # 返回新建的顺序串

    def rep_str(self, i, j, t):
        """串替换"""
        s = SqString()  # 新建一个空串
        assert 0 <= i < self.size and j > 0 and i + j <= self.size  # 检测参数
        for k in range(i):  # 将当前串data[0..i-1]->s
            s.data[k] = self.data[k]
        for k in range(t.getsize()):  # 将s.data[0..t.size-1]→s
            s.data[i + k] = t.data[k]
        for k in range(i + j, self.size):  # 将当前串data[i+j..size-1]->s
            s.data[t.getsize() + k - j] = self.data[k]
        s.size = self.size - j + t.getsize()
        return s  # 返回新建的顺序串

    def disp_str(self):
        """输出串"""
        for i in range(self.size):
            print(self.data[i], end='')
        print()

    def str_cmp(self, t):
        """比较两个字符串的大小"""
        minl = min(self.getsize(), t.getsize())  # 求s和t中最小长度
        for i in range(minl):  # 在共同长度内逐个字符比较
            if self[i] > t[i]:
                return 1
            elif self[i] < t[i]:
                return -1
        if self.getsize() == t.getsize():  # s==t
            return 0
        elif self.getsize() > t.getsize():  # s>t
            return 1
        else:
            return -1  # s<t


if __name__ == '__main__':
    cstr1 = "abcd"
    cstr2 = "123"
    s1 = SqString()
    s1.str_assign(cstr1)
    print("s1: ", end='')
    s1.disp_str()
    print("s1的长度: %d" % s1.getsize())
    s2 = SqString()
    s2.str_assign(cstr2)
    print("s2: ", end='')
    s2.disp_str()
    print("s2的长度: %d" % s2.getsize())
    print("s1=>s3")
    s3 = s1.str_copy()
    print("s3: ", end='')
    s3.disp_str()
    print("s1和s2连接=>s4")
    s4 = s1.concat(s2)
    print("s4: ", end='')
    s4.disp_str()
    print("s4[2...5]=>s5")
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
