s = []
for i in range(1, 5):
    for n in range(1, 5):
        for m in range(1, 5):
            if i != n and n != m and i != m:  # 判断数字重复
                a = str(i) + str(n) + str(m)
                s.append(int(a))
print("可以组成的三位数有：{}，共有{}个".format(s, len(s)))
