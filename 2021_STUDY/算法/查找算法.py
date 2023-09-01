from random import *

n = int(input("请输入统计的学生人数："))
grade = []
for i in range(n):
    num = randint(1000, 10000)  # 生成学号
    score = randint(30, 100)  # 生成成绩
    x = [num, score]
    grade.append(x)  # 将学号、成绩构成一个列表
print("学生信息：", grade)
cx = int(input("请输入要查成绩的学生学号，在1000-9999之间："))
flag = False
for y in range(n):
    if cx == grade[y][0]:
        flag = True
        break
if flag:
    print("您查找的学号为：{},成绩为：{}".format(grade[y][0], grade[y][1]))
else:
    print("未找到查询的信息")  # 输出结果
