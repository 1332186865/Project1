lst = [10, 30, 50, 70, 90, 130, 150, 170]
x = eval(input('请输入要查找的数：'))
f = False
i = -1
low = 0
high = len(lst) - 1
while low <= high:
    mid = int((low + high) // 2)
    if x == lst[mid]:
        f = True
        i = mid
        break
    elif x < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1
if f:
    print('找到', x, '位置为', i)
else:
    print('未找到', x)
