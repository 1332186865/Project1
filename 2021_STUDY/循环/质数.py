from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
b = True
for x in range(2, end + 1):
    if num % x == 0:
        b = False
        break
if b and num != 1:
    print('%d是质数' % num)
else:
    print('%d不是质数' % num)
