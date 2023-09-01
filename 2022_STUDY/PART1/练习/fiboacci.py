#  Copyright (c) 2022. Generated by Gu.
def fibonacci(n):
    count = 0  # 记录当前生成数的个数
    if count >= n:
        return
    yield 1
    count += 1

    if count >= n:
        return
    yield 1
    count += 1
    # 用列表生成第三个之后的数
    # ls = [1, 1]
    a = 1  # 倒数第二个数
    b = 1  # 倒数第一个数
    while count < n:
        # ls.append(ls[-1] + ls[-2])
        # yield ls[-1]
        a, b = b, a + b
        yield b
        count += 1


# 输出前二十个数
for x in fibonacci(20):
    print(x)
# 求前三十个数的和
print(sum(fibonacci(30)))
