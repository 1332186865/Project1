def read_input():
    ls = []
    while True:
        s = input("请输入：")
        if not s:
            break
        ls.append(s)
    return ls


def write_input(ls):
    try:
        f = open('1.txt', 'w')
        for line in ls:
            f.write(line)
            f.write('\n')
        f.close()
    except IOError:
        print("写文件失败")


def read_input_file(filename='1.txt'):
    f = open(filename)
    ls = []
    while True:
        s = f.readline()
        if not s:
            break
        s = s.rstrip()
        ls.append(s)
    f.close()
    return ls


def print_file_info(lst):
    for line in enumerate(lst, 1):
        print('第%d行：%s' % line)


def main():
    lst = read_input()
    print(lst)
    write_input(lst)
    lst = read_input_file()
    print_file_info(lst)


if __name__ == '__main__':
    main()
