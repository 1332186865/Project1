a = 1
b = 1
n = 2
print("{:^3} {:^3}".format(a, b), end=' ')
while n < 20:
    a, b = b, a + b
    n += 1
    print("{:^3}".format(b), end=' ')
    if n % 10 == 0:
        print()
