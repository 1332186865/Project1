def sjx(a, b, c):
    if a + b > c and a + c > b and b + c > a:  # 判断能否构成三角形
        print('周长：%.2F' % (a + b + c))  # 输出周长
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积：{:.2F}'.format(area))  # 输出面积
    else:
        print('不能构成三角形！')  # 输出另一种结果
    return


x = float(input('x='))
y = float(input('y='))
z = float(input('z='))  # 输入数据
print(sjx(x, y, z))  # 输出
