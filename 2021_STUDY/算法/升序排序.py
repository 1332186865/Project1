from random import *  # 导入库


def px(x):
    ls = []
    for i in range(x):
        ls.append(randint(100, 999))  # 生成随机数
    print('原列表为：', ls)
    for i in range(len(ls) - 1):
        k = i  # 假定第i个元素为最小值
        for j in range(i + 1, len(ls)):
            if ls[k] > ls[j]:
                k = j  # 记录下最小元素的索引
        ls[i], ls[k] = ls[k], ls[i]  # 排序
    return ls


n = int(input('请输入整数个数：'))
print('排序后的列表为：', px(n))
