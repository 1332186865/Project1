Sn = 100.0
Hn = Sn / 2
for n in range(2, 11):
    Sn += 2 * Hn
    Hn /= 2
print('the sum length of path: %f' % Sn)
print('the last height is: %.8f ' % Hn)
