def xsxx():  # 学生信息
    id = input("请输学号 ：")
    name = input("请输姓名 ：")
    gs = eval(input("请输高数 ："))
    yy = eval(input("请输英语 ："))
    jsj = eval(input("请输计算机 ："))
    r = [id, name, gs, yy, jsj]  # 学生信息组织为一维列表
    return r


def xszf(xs):  # 学生总分
    r = sum(xs[2:5])  # 计算总分
    return r


def kcpjf(f):  # 课程平均分
    s = 0
    p = 0
    for x in f:  # 计算总分
        p += 1
        s += x
    o = s / p
    return o


n = int(input("学生人数n= "))
cjb = []  # 成绩表
math = []  # 数学
english = []  # 英语
computer = []  # 计算机
for i in range(n):
    biao = xsxx()
    cjb.append(biao)
for v in cjb:
    total = xszf(v)
    print("学生{}，总分为：{}".format(v, total))
for kc in cjb:
    math.append(kc[2])
    english.append(kc[3])
    computer.append(kc[4])
print("数学平均分{}，最高分{}，最低分{}".format(kcpjf(math), max(math), min(math)))
print("英语平均分{}，最高分{}，最低分{}".format(kcpjf(english), max(english), min(english)))
print("计算机平均分{}，最高分{}，最低分{}".format(kcpjf(computer), max(computer), min(computer)))
