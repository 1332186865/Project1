x = float(input("请输入里程："))
y = 0
if x <= 3:
    y += 10
elif x <= 10:
    y = y + 10 + 1.2 * (x - 3)
elif x <= 20:
    y = y + 10 + 1.2 * (10 - 3) + 1.5 * (x - 10)
else:
    y = y + 10 + 1.2 * (10 - 3) + 1.5 * (20 - 10) + 2.5 * (x - 20)
print("价钱为：", y)
