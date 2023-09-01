L = [1, 2, 3, 4, 5]
S = [0, 9, 8, 7, 6, 5]


def fx(list1, list2):
    ls1 = iter(list1)
    ls2 = iter(list2)
    try:
        while True:
            a = next(ls1)
            b = next(ls2)
            yield a, b
    except StopIteration:
        pass


apple = fx(L, S)
for i in range(5):
    print(next(apple))
