m = str(input('请输入一个英文句子：'))
n = m.split()
a = 0
b = 0
for i in n:
    while len(i) > a:
        a = len(i)
        b = i
print('最长单词为{}, 长度为{}'.format(b, a))
