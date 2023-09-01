class SqList:
    def __init__(self):  # 构造方法
        self.initcapacity = 5  # 初始容量5
        self.capacity = self.initcapacity  # 容量
        self.data = [None] * self.capacity  # 顺序表空间
        self.size = 0  # 长度

    def resize(self, newcapacity):
        """改变顺序表容量"""
        assert newcapacity >= 0
        olddata = self.data
        self.data = [None] * newcapacity
        self.capacity = newcapacity
        for i in range(self.size):
            self.data[i] = olddata[i]

    def creatlist(self, a):
        """由数组a元素整体建立数据表"""
        for i in range(0, len(a)):
            if self.size == self.capacity:  # 出现溢出
                self.resize(2 * self.size)  # 扩大容量
            self.data[self.size] = a[i]  # 添加元素
            self.size += 1  # 长度增加

    def add(self, e):
        """末尾添加元素e"""
        if self.size == self.capacity:  # 倍增容量
            self.resize(2 * self.size)
        self.data[self.size] = e  # 添加元素
        self.size += 1  # 长度增1

    def getsize(self):
        """顺序表长度"""
        return self.size

    def __getitem__(self, i):
        """求序号i的元素值"""
        assert 0 <= i < self.size
        return self.data[i]

    def __setitem__(self, key, value):
        """设置序号i的元素值"""
        assert 0 <= key < self.size
        self.data[key] = value

    def getno(self, e):
        """查找第一个为e的元素的序号"""
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1  # 查找元素e
        if i >= self.size:  # 未找到返回-1
            return -1
        else:
            return i  # 找到返回序号

    def insert(self, i, e):
        """在顺序表序号i处插入元素e"""
        assert 0 <= i <= self.size
        if self.size == self.capacity:
            self.resize(2 * self.size)  # 满则倍增容量
        for j in range(self.size, i - 1, -1):  # 将data[i]后元素后移一个位置
            self.data[j] = self.data[j - 1]
        self.data[i] = e  # 插入元素e
        self.size += 1  # 长度增1

    def delete(self, i):
        """删除序号i的元素"""
        assert 0 <= i <= self.size - 1
        for j in range(i, self.size - 1):
            self.data[j] = self.data[j + 1]  # data[i]后元素前移
        self.size -= 1  # 长度-1
        if self.capacity > self.initcapacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)  # 满足缩容条件则容量减半

    def display(self):
        """输出顺序表"""
        for i in range(0, self.size):
            print(self.data[i], end=' ')
        print()

    def reverse(self):
        """逆置"""
        i = 0
        j = self.getsize() - 1
        while i < j:
            self[i], self[j] = self[j], self[i]
            i += 1
            j -= 1

    def deletek(self, i, k):
        """删除从序号i开始的k个元素"""
        assert i >= 0 and k >= 1 and 1 <= i + k < self.getsize()
        for j in range(i + k, self.getsize()):
            self[j - k] = self[j]
        self.size -= k

    def deletex1(self, x):
        """删除所有指定元素x"""
        k = 0
        for i in range(self.getsize()):
            if self[i] != x:
                self[k] = self[i]
                k += 1
        self.size = k

    def merger2(self, B):
        """合并两个表为递增有序线性表 时空复杂度O(m+n)"""
        C = SqList()
        i = j = 0
        while i < self.getsize() and j < B.getsize():
            if self[i] < B[j]:
                C.add(self[i])
                i += 1
            else:
                C.add(B[j])
                j += 1
        while i < self.getsize():
            C.add(self[i])
            i += 1
        while i < B.getsize():
            C.add(B[j])
            j += 1
        return C

    def middle(self, B):
        """将两个表合并为有序线性表，并找出中位数"""
        # 序号为n-1的是中位数
        i = j = k = 0
        while i < self.getsize() and j < B.getsize():
            k += 1
            if self[i] < B[j]:
                if k == self.getsize():  # 恰好比较n次
                    return self[i]
            else:
                if k == B.getsize():
                    return B[j]
                j += 1


a1 = SqList()
a1.add(1)
a1.add(2)
a1.add(3)
a1.add(4)
a1.add(5)
a1.display()
