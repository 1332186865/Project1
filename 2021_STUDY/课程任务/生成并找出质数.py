def zs(sz):
    for r in range(2, sz):
        if sz % r == 0:
            return False
    return True  # 判断质数


def zsqh(d):
    s = 0
    for h in d:
        s += h
    return s  # 求质数和


a = '56,41,70,31,83'  # 正整数数据
b = a.split(',')
print('原数据为：{}，共计{}个数据'.format(a, len(b)))
c = []
for i in b:
    if zs(int(i)):
        c.append(int(i))
print('其中质数为：{},共计{}个质数'.format(c, len(c)))
print('质数和为：{}'.format(zsqh(c)))  # 输出结果
