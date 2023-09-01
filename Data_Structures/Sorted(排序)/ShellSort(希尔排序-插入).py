def ShellSort(R):  # 对R[0..n-1]按递增有序进行希尔排序
    d = len(R) // 2  # 增量置初值
    while d > 0:
        for i in range(d, len(R)):  # 对所有相隔d位置的元素组采用直接插入排序
            if R[i] < R[i - d]:  # 反序时
                tmp = R[i]
                j = i - d
                while True:
                    R[j + d] = R[j]  # 将大于tmp的元素后移
                    j = j - d  # 继续向前找
                    if j < 0 or R[j] <= tmp: break  # 若j<0或者R[j]<=tmp,退出循环
                R[j + d] = tmp  # 在j+d处插入tmp
        d = d // 2  # 递减增量


# 主程序
if __name__ == '__main__':
    R = [1, 6, 3, 4, 2, 5, 8, 7]
    #    R=[9,8,7,6,5,4,3,2,1]
    print("初始序列", end=' ')
    print(R)
    print("排序")
    ShellSort(R)
    print("排序序列", end=' ')
    print(R)
