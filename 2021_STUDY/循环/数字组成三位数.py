index = [2, 3, 4, 0]
s = 0
for i in index:
    for a in index:
        for b in index:
            if a == b or a == i or b == i or i == 0:
                continue
            else:
                s += 1
                print(str(i) + str(a) + str(b), end=' ')
print('')
print('满足条件的有', s, '个')
