#  Copyright (c) 2022. Generated by Gu.
#  本程序示意自定义的类作为环境管理器使用
class Filewriter:
    def __init__(self, filename):
        self.filename = filename  # 记住文件名

    def write(self, abc):
        """向文件内写入字符串，同时自动添加换行"""
        self.file.write(abc)
        self.file.write('\n')

    def __enter__(self):
        """此方法用于实现环境管理器"""
        self.file = open(self.filename, 'w')
        print("进入__enter__方法，文件打开成功")
        return self  # 返回值用于with中的as绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        """exec_type 为异常类型, 没有异常发生时为None
           exec-value为错误的对象, 没有异常时为None
           exec_tb   为错误的traceback对象"""
        self.file.close()
        print("文件", self.filename, "已经关闭")
        if exc_type is None:
            print("退出with时没有发生异常")
        else:
            print("退出with时,有异常,类型是", exc_type, "错误是", exc_val)
        print("__exit__方法被调用， 已离开with语句")


with Filewriter('abcd.txt') as fw:
    while True:
        s = input("请输入一行：")
        if s == 'exit':
            break
        if s == 'error':
            raise ValueError('值错误！')
        fw.write(s)

print("这是with语句之外,也是程序的最后一条语句")
