'''
def InsertSort(R): 				    #对R[0..n-1]按递增有序进行直接插入排序
    for i in range(1,len(R)):		#从第2个元素即R[1]开始
        if R[i]<R[i-1]:     		#反序时
            tmp=R[i]				#取出无序区的第一个元素
            j=i-1;					#在有序区R[0..i-1]中从右向左找R[i]的插入位置
            while True:
                R[j+1]=R[j]			#将大于tmp的元素后移
                j-=1				#继续向前比较
                if j<0 or R[j]<=tmp: break  #若j<0或者R[j]<=tmp,退出循环
            R[j+1]=tmp				#在j+1处插入R[i]
'''


def cmp(x, y):
    if x >= y:
        return True
    else:
        return False


def InsertSort(R):  # 对R[0..n-1]按递增有序进行直接插入排序
    for i in range(1, len(R)):  # 从第2个元素即R[1]开始
        if cmp(R[i], R[i - 1]):  # 反序时
            tmp = R[i]  # 取出无序区的第一个元素
            j = i - 1  # 在有序区R[0..i-1]中从右向左找R[i]的插入位置
            while True:
                R[j + 1] = R[j]  # 将大于tmp的元素后移
                j -= 1  # 继续向前比较
                if j < 0 or not cmp(tmp, R[j]): break  # 若j<0或者R[j]<=tmp,退出循环
            R[j + 1] = tmp  # 在j+1处插入R[i]


# 主程序
if __name__ == '__main__':
    R = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("初始序列", end=' ')
    print(R)
    print("排序")
    InsertSort(R)
    print("排序序列", end=' ')
    print(R)
