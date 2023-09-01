n = 5
m = 1
a = 0
i = 1
while n >= i:
    m *= i
    a += m
    i += 1
print("1!+2!+3!+4!+5!=", a)

n = 1
s = 0
for i in range(1, 6):
    n *= i
    s += n
print(s)
