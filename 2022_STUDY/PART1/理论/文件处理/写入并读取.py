file = open("a.txt", 'w')
file.write("python语言程序设计教程\n")
file.write("主编赵璐")
file.close()  # 写入文件
file = open("a.txt", 'r')
c = file.readline()
a, b = 0, 0
print('文件内容：')
while c != '':
    print(c, end='')
    a += 1
    b += len(c)
    c = file.readline()  # 统计字数
print('\n字数{}， 行数{}'.format(b, a))
