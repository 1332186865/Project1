def Merge(R, low, mid, high):  # R[low..mid]和R[mid+1..high]归并为R[low..high]
    R1 = [None] * (high - low + 1)  # 分配临时归并空间R1
    i, j, k = low, mid + 1, 0  # k是R1的下标,i、j分别为第1、2段的下标
    while i <= mid and j <= high:  # 在第1段和第2段均未扫描完时循环
        if R[i] <= R[j]:  # 将第1段中的元素放入R1中
            R1[k] = R[i]
            i, k = i + 1, k + 1
        else:  # 将第2段中的元素放入R1中
            R1[k] = R[j]
            j, k = j + 1, k + 1
    while i <= mid:  # 将第1段余下部分复制到R1
        R1[k] = R[i]
        i, k = i + 1, k + 1
    while j <= high:  # 将第2段余下部分复制到R1
        R1[k] = R[j]
        j, k = j + 1, k + 1
    R[low:high + 1] = R1[0:high - low + 1]


def MergePass(R, length):  # 一趟二路归并排序
    n = len(R)
    i = 0
    while i + 2 * length - 1 < n:  # 归并length长的两相邻子表
        Merge(R, i, i + length - 1, i + 2 * length - 1)
        i = i + 2 * length
    if i + length < n:  # 余下两个子表,后者长度小于length
        Merge(R, i, i + length - 1, n - 1)  # 归并这两个子表


def MergeSort1(R):  # 对R[0..n-1]按递增进行二路归并算法
    length = 1
    while length < len(R):  # 进行log2n(取上界)趟归并
        MergePass(R, length)
        length = 2 * length


def MergeSort2(R):  # 对R[0..n-1]按递增进行二路归并算法
    MergeSort21(R, 0, len(R) - 1)


def MergeSort21(R, s, t):  # 被MergeSort2调用
    if s >= t: return  # R[s..t]的长度为0或者1时返回
    m = (s + t) // 2  # 取中间位置m
    MergeSort21(R, s, m)  # 对前子表排序
    MergeSort21(R, m + 1, t)  # 对后子表排序
    Merge(R, s, m, t)  # 将两个有序子表合并成一个有序表


# 主程序
if __name__ == '__main__':
    # R=[9,8,7,6,5,4,3,2,1]
    R = [3, 2, 1]
    print("初始序列", end=' ')
    print(R)
    print("排序")
    MergeSort2(R)
    print("排序序列", end=' ')
    print(R)
