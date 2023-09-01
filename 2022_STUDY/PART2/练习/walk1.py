# 1.小明家必须要过一座桥。小明过桥最快要１秒，小明的弟弟最快要３秒，小明的爸爸最快要６秒，小明的妈妈最快要８秒，小明的爷爷最快要１２秒。每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。小明一家该如何过桥，请写出详细过程。

# 1  3  6  8  12

# 思路   多走几次快的人
# 3+1+6+1+8+1+12 = 32s

# 思路二 慢的人尽量少走  (8和12 一起走)
# A岸
# B岸  8 12  6 3 1
# 小明和弟弟先走  耗时3
# 小明送手电筒       1
# 妈妈和爷爷过桥  耗时12
# 弟弟送手电筒       3
# 小明和爸爸过桥     6
# 小明送手电筒      1
# 小明和弟弟过桥    3
# 共29s


# 代码 随机找人从a岸到b岸去 统计每次的时间  直到有一次时间小于30为止
import random

while True:
    a = [1, 3, 6, 8, 12]  # a岸的人
    b = []  # b岸的人
    timer = 0  # 时间
    step = []  # 过程

    while True:
        # 从a中随机获取2个不重复的值
        x = random.sample(a, 2)
        # 将x放入b中
        b.extend(x)
        # 删除a中的x的值
        a.remove(x[0])
        a.remove(x[1])
        step.append(x)  # 将组合记录到过程列表
        step.append(max(x))  # 将过河时间记录到列表
        # a中没有人了 不要回来  结束循环
        if not a:
            break

        # b中的一个人回来(最快的人回来)
        y = min(b)
        a.append(y)
        b.remove(y)
        step.append(y)  # 既是记录人过河  也记录时间
        step.append('||')  # 分隔符

    # 取出所有的表示时间的数字 累加到timer
    for i in step:
        if type(i) == int:
            timer += i

    if timer <= 30:
        print(timer)
        break
# 打印过程
print(step)
