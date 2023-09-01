import math

x = float(input("请输入一个实数："))
n = 0
y = 1.0
while abs(y * y - x) > 1e-8:
    y = (y + x / y) / 2
    n = n + 1
    print(n, y)
print("平方根为：", y)
print("sqrt求平方根为：", math.sqrt(x))
