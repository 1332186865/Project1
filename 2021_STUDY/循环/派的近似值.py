import math

a = pow(10, (-4))
x = 0
n = 1
pai = 0
while a < 1 / (n ** 2):
    x += (1 / (n ** 2))
    n += 1
pai = math.sqrt(6 * x)
print('派的近似值是：', pai)
