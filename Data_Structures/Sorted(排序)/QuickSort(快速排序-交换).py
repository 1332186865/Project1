#  Copyright (c) 2022. Generated by Gu.
def partition(R, s, t):
    i, j = s, t
    base = R[s]  # 以表首元素为基准
    while i != j:  # 从表两端交替向中间遍历,直至i=j为止
        while j > i and R[j] >= base:
            j -= 1  # 从后向前遍历,找一个小于基准的R[j]
        if j > i:
            R[i] = R[j]  # R[j]前移覆盖R[i]
            i += 1
        while i < j and R[i] <= base:
            i += 1  # 从前向后遍历,找一个大于基准的R[i]
        if i < j:
            R[j] = R[i]  # R[i]后移覆盖R[j]
            j -= 1
    R[i] = base  # 基准归位
    return i  # 返回归位的位置


def quickSort(R):  # 对R[0..n-1]的元素按递增进行快速排序
    quickSort1(R, 0, len(R) - 1)


def quickSort1(R, s, t):  # 对R[s..t]的元素进行快速排序
    if s < t:  # 表中至少存在两个元素的情况
        i = partition(R, s, t)
        quickSort1(R, s, i - 1)  # 对左子表递归排序
        quickSort1(R, i + 1, t)  # 对右子表递归排序


if __name__ == '__main__':
    R = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("未排序", R)
    quickSort(R)
    print("排序后", R)
