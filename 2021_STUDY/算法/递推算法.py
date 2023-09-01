a = 1
b = 2
s = 0  # 赋初值
i = 0
for i in range(20):  # 循环20次
    s += b / a
    a, b = b, (a + b)
print(s)
