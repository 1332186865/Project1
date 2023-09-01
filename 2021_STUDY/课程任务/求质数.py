s = 0  # 计数器
for i in range(100, 1000):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False  # 判断质数
    if flag:
        print(i, end=' ')
        s += 1
        if s % 5 == 0:
            print()  # 格式化输出结果
