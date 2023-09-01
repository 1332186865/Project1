a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
zd = 0
zx = 0
if a > b:
    zd = a
    zx = b
else:
    zd = b
    zx = a
if zd < c:
    zd = c
if zx > c:
    zx = c
print("最大值是：", zd)
print("最小值是：", zx)
