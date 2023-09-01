def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)
        bar()
        # print(c)


if __name__ == '__main__':
    a = 100
    foo()
