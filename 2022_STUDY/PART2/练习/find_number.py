"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。1 <= 数组长度 <= 10000
输入:  [0,1,2,3,4,5,6,7,8]
示例:  0,1,2,3,4,5,6,7,8    索引
输入: [0,1,2,3,4,5,7,8,9]    范围0~9   1-n    (n+1)*n/2
输出: 9     n-1=9   n=10   长度：9   值：0~9（10个数字）
"""
"""
算法：题海战术         做至少30道算法题
"""


# 方法1

def find_num(ls):
    # 从头到尾连续的情况
    if ls[-1] == len(ls) - 1:
        return len(ls)
    # 从头到尾不连续的情况
    for i in range(len(ls)):
        if i != ls[i]:
            return i


list_target = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(find_num(list_target))


# 方法2 :数学公式法
def find_num1(list_target):
    n = len(list_target)
    return (n + 1) * n // 2 - sum(list_target)


list_target = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(find_num1(list_target))
