# 给定一个只有A，C，M三个字母组成的字符串且长度不超过10000000。如果字符串中存在“ACM”子串，那么这个“ACM”子串可以自动消掉，消掉后，后面的元素都前移再变成一个新的完整的字符串。
# 这个新串继续这样做，直到被消成空串或不再有”ACM”子串。GGS的任务是判断给定的字符串是否能被消为空串，如果可以，那么输出YES,否则输出NO。
# 输入一个字符串只含有A,C,M（大写）且非空
# 输出YES或NO，输出单独占一行。
class SqStack:
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


# 方法一（有问题）
a = input()
while len(a):
    index = -1
    for i in range(len(a)):
        if a[i] == 'A' and a[i + 1] == 'C' and a[i + 2] == 'M':
            index = i
            break
    if index == -1:
        break
    else:
        a = a.replace("ACM", "")

if len(a) == 0:
    print("Yes")
else:
    print("No")

# 方法二（未完成）
"""
def isTrue(str1):
    sq = SqStack()
    cnt = 0
    str2 = "ACM"
    if len(str1) % 3 == 0:
        return False
    for i in range(len(str1), 3):
        sq.push(str1[i])
        sq.push(str1[i])
        sq.push(str1[i])
        while not sq.empty() and (sq.gettop() == str2[cnt]):
            sq.pop()  # 出栈
            cnt += 1
    return sq.empty()


a = input()
if isTrue(a):
    print('Yes')
else:
    print('No')
"""

# 方法三
a, c, m = 0, 0, 0
flag = 1
str1 = input()
for ch in str1:
    if ch == "M":
        m += 1
    elif ch == "A":
        a += 1
    elif ch == "C":
        c += 1
    if c > a or m > c or m > a or (ch == "C" and s == "C"):
        flag = 0
        break
    s = ch
if c != a or c != m or m != a:
    flag = 0
if flag:
    print("YES")
else:
    print("NO")
