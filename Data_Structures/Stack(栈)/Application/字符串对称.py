# 给定一个中缀表达式，请编写程序计算该表达式的值。表达式包含+、-、*、\、(、)，所有运算均为二元运算，操作数均为正整数，但可能不止一位，不超过5位。运算结果为整数，值域为[−2^31 ,2^31)。
# 除法运算结果若为小数则进行截尾取整。若除法运算中除数为0，则输出ILLEGAL。
# 5+(10*2)-6 19
# 8*(999+1) 8000
# 1+5/(1-1) ILLEGAL

class Sqstack:
    def __init__(self):
        self.data = []

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 进栈
        self.data.append(e)

    def pop(self):  # 出栈
        assert not self.empty()
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.data[-1]


def isPalindrome(str1):
    st = Sqstack()  # 建立顺序栈
    n = len(str1)
    i = 0
    while i < n // 2:  # 将str前半字符进栈
        st.push(str1[i])
        i += 1
    if n % 2 == 1:  # n为奇数跳过
        i += 1
    while i < n:  # 遍历后半字符
        if st.pop() != str1[i]:
            return 'no'
        i += 1
    return 'yes'


str = "abcba"
print(isPalindrome(str))
