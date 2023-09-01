from random import *  # 导入库

a = int(input("请输入学生人数："))
b = []
for i in range(a):
    b.append(randint(30, 100))  # 创建成绩列表
print('排序前的成绩为：', b)
for c in range(a - 1):
    k = c
    for d in range(c + 1, a):
        if b[k] < b[d]:
            k = d
    b[c], b[k] = b[k], b[c]  # 排序
print('排序后的成绩为：', b)
