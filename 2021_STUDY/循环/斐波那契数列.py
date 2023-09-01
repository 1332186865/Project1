def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    for val in fib(20):
        print("{:>3}".format(val), end=' ')
    print()
    for val in range(1, 21):
        print("{:>3}".format(fibo(val)), end=' ')


if __name__ == '__main__':
    main()
