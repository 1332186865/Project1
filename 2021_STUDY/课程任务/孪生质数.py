def lsss(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True  # 判断质数


for a in range(2, 501):
    if lsss(a) and lsss(a + 2):  # 判断质数及其孪生质数
        print("({:^3}, {:^3})".format(a, a + 2))  # 输出结果
