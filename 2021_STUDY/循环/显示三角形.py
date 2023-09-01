row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
        print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

# 利用二维列表生成n行杨辉三角，n由键盘输入。杨辉三角的规律是：第一列和对角线元素均为1，其余元素是该元素头顶元素与左肩元素之和，
# 可以通过公式计算得到：yh[i][j]=yh[i-1][j-1]+yh[i-1][j]
# n行杨辉三角
n = int(input("请输入杨辉三角的行数："))
yanghui = []
for i in range(n):
    yanghui.append([1 for _ in range(n)])
for i in range(1, n):
    for j in range(1, i):
        yanghui[i][j] = yanghui[i - 1][j - 1] + yanghui[i - 1][j]
for i in range(0, n):
    for j in range(0, i + 1):
        print('{:3d}'.format(yanghui[i][j]), end='')
    print()
