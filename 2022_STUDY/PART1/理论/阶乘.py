# 递归
def fact1(n):
    if n == 1:
        return 1
    return fact1(n - 1) * n


def fact2(n):
    if n == 1:
        r = fact2(n - 1) * n
    else:
        r = 1
    return r


# 循环
def fact3(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s


# 高阶函数阶乘和
def mysum(n):
    return sum(map(fact1(n), range(1, n + 1)))
