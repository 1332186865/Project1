grades = {}
s = 0
while s < 10:
    n = str(input('请输入学生姓名：'))
    if n == '':
        break
    a = float(input('请输入学生英语成绩：'))
    b = float(input('请输入学生数学成绩：'))
    c = (a + b) / 2
    grades[n] = c
    s += 1
for x, y in grades.items():
    print(f'{x}的平均成绩是{y:.5f}')
