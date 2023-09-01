# 顺序表查找
def SeqSearch1(R, k):  # 顺序查找算法1
    n = len(R)
    i = 0
    while i < n and R[i] != k: i += 1  # 从表头往后找
    if i >= n:
        return -1  # 未找到返回-1
    else:
        return i  # 找到后返回其序号i


def SeqSearch2(R, k):  # 顺序查找算法2
    n = len(R)
    R.append(k)  # 添加哨兵
    i = 0
    while R[i] != k: i += 1  # 从表头往后找
    if i == n:
        return -1  # 未找到返回-1
    else:
        return i  # 找到后返回其序号i


if __name__ == '__main__':
    R = [3, 9, 1, 5, 8, 10, 6, 7, 2, 4]
    k = 6
    print(SeqSearch1(R, k))
    print(SeqSearch2(R, k))
