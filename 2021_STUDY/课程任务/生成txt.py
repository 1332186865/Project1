f1 = open('D:\\Personal\\Desktop\\学生成绩表.txt', 'w')
n = int(input('请输入学生人数：'))
s = 0
while s < n:
    a = input('学号')
    b = input('姓名')
    c = input('高数成绩')
    d = input('英语成绩')
    e = input('计算机成绩')
    f1.writelines(['{}\t, {}\t, {}\t, {}\t, {}\n'.format(a, b, c, d, e)])
    s += 1
