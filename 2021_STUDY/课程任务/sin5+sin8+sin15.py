import math  # 导入库


def jc(y):
    s = 1
    for i in range(1, y + 1):
        s *= i  # 累乘
    return s  # 阶乘函数


def mysin(x):
    while x > math.pi:
        x -= 2 * math.pi  # 如果x>二派，则减去两个派
    a = x - x ** 3 / jc(3) + x ** 5 / jc(5) - x ** 7 / jc(7) + x ** 9 / jc(9) - x ** 11 / jc(11)
    return a


m = mysin(5) + mysin(8) + mysin(15)
print('sin5+sin8+sin15=', m)  # 计算最终结果
