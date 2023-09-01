print("-------算法1-------")
a = [100]
print(id(a))


def test(x):
    x = x + x
    print(x)


test(a)
print(id(a))
print(a)

print("-------算法2-------")
a = [100]
print(id(a))


def test(x):
    x += x  # 此处与上题不同。结果也会不同
    print(x)


test(a)
print(id(a))
print(a)
