# 帕多瓦数列
class Pauda:
    def __init__(self, num):
        self.lst = [0, 1, 1, 1]
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.lst.append(self.lst[-2] + self.lst[-3])
        self.count += 1
        if self.count < self.num:
            return self.lst[self.count]
        else:
            raise StopIteration


pauda = Pauda(20)
print(list(pauda))
