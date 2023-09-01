x = [13, 5, 17, 12, 9, 2, 8]
n = len(x)
print("排序前:", x)
for i in range(1, n):  # 外循环，插入数据的次数
    t = x[i]  # 用t记录当前元素
    j = i - 1
    while j > 0:  # 内循环，元素逐一后移，腾出空位
        if x[j] < t:
            x[j + 1] = x[j]
            x[j] = t
        j -= 1
print("排序后：", x)
