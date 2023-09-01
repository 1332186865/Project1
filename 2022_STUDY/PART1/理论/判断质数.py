def su(x):  # 定义函数
    for i in range(2, x):
        if x % i == 0:
            return False  # 可被整除返回否
    return True  # 不可被整除返回是


s = 0  # 计数器
for a in range(100, 201):
    if su(a):
        s += 1
        print(a, end=' ')  # 输出结果
        if s % 6 == 0:
            print()  # 换行
