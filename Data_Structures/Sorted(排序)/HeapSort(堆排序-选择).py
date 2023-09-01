def sift_down(R, low, high):  # R[low..high]的自顶向下筛选
    i = low
    j = 2 * i + 1  # R[j]是R[i]的左孩子
    tmp = R[i]  # tmp临时保存根结点
    while j <= high:  # 只对R[low..high]的元素进行筛选
        if j < high and R[j] < R[j + 1]:
            j += 1  # 若右孩子较大,把j指向右孩子
        if tmp < R[j]:  # tmp的孩子较大
            R[i] = R[j]  # 将R[j]调整到双亲位置上
            i, j = j, 2 * i + 1  # 修改i和j值,以便继续向下筛选
        else:
            break  # 若孩子较小，则筛选结束
    R[i] = tmp  # 原根结点放入最终位置


def sift_up(R, j):  # 自底向上筛选:从叶子结点i向上筛选
    i = (j - 1) // 2  # i指向R[j]的双亲
    while True:
        if R[j] > R[i]:  # 若孩子较大
            R[i], R[j] = R[j], R[i]  # 交换
        if i == 0:
            break  # 到达根结点时结束
        j = i
        i = (j - 1) // 2  # 继续向上调整


def heap_sort(R):  # 对R[0..n-1]按递增进行堆排序
    n = len(R)
    for j in range(n // 2, n - 1):  # 循环建立初始堆
        sift_up(R, j)  # 对R[j]的叶子结点进行筛选
    for i in range(n - 1, 0, -1):  # 进行n-1趟排序,每一趟排序的元素个数减1
        R[0], R[i] = R[i], R[0]  # 将区间中最后一个元素与R[0]交换
        sift_down(R, 0, i - 1)  # 对R[0..i-1]]继续筛选


R = [88, 29, 65, 95, 41, 22, 61, 54, 23, 10]
print("初始序列", R)
heap_sort(R)
print("排序序列", R)
