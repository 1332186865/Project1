def SelectSort(R):  # 对R[0..n-1]元素进行简单选择排序
    for i in range(len(R) - 1):  # 做第i趟排序
        minj = i  # minj先置为区间中的首元素序号
        for j in range(i + 1, len(R)):  # 从R[i..n-1]中选最小元素的R[minj]
            if R[j] < R[minj]:  # 与区间中其他元素比较
                minj = j
        if minj != i:  # R[minj]不是无序区首元素
            R[i], R[minj] = R[minj], R[i]  # 交换R[i]和R[minj]


# 主程序
if __name__ == '__main__':
    R = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("初始序列", end=' ')
    print(R)
    print("排序")
    SelectSort(R)
    print("排序序列", end=' ')
    print(R)
