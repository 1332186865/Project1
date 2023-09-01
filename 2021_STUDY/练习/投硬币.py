import random  # 加载库

s = [0, 0]
for i in range(10000):
    m = random.randint(0, 1)  # 生成随机数
    s[m] += 1
z = s[0] / 10000
f = s[1] / 10000  # 求比率
print('正面出现的概率为{:.2%}，反面出现的概率为{:.2%}'.format(z, f))  # 格式化输出
