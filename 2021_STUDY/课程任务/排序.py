from random import *  # 导入random

cj = []
for n in range(30):
    cj.append(randint(30, 100))  # 取随机数
print("排序之前的数据为", cj)
sl = len(cj)
for i in range(sl - 1):
    k = i
    for j in range(i + 1, sl):  # 从下一个元素开始比较
        if cj[k] > cj[j]:
            k = j
    cj[i], cj[k] = cj[k], cj[i]  # 交换元素位置
print("排序之后的数据为", cj)
