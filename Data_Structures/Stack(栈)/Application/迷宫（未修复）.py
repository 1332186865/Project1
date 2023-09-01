class Sqstack:
    def __init__(self):
        self.data = []

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 进栈
        self.data.append(e)

    def pop(self):  # 出栈
        assert not self.empty()
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.data[-1]


class Box:
    def __init__(self, i1, j1, di1):
        self.i = i1
        self.j = j1
        self.di = di1


def mgpath(xi, yi, xe, ye):
    global mg
    st = Sqstack()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    e = Box(xi, yi, -1)
    st.push(e)
    mg[xi][yi] = -1
    while not st.empty():
        b = st.gettop()
        if b.i == xe and b.j == ye:
            for k in range(len(st.data)):
                print("[" + str(st.data[k].i) + ',' + str(st.data[k].j) + "]", end='')
            return True
        find = False
        di = b.di
        while di < 3 and not find:
            di += 1
            i, j = b.i + dx[di], b.j + dy[di]
            if mg[i][j] == 0:
                find = True
        if find:
            b.di = di
            b1 = Box(i, j, -1)
            st.push(b1)
            mg[i][j] = -1
        else:
            mg[b.i][b.j] = 0
            st.pop()
    return False


n = int(input())
mg = [input().split(' ') for i in range(n)]
for i in range(len(mg)):
    mg[i] = list(map(int, mg[i]))
xi, yi, xe, ye = input().split(' ')
mgpath(int(xi), int(yi), int(xe), int(ye))
