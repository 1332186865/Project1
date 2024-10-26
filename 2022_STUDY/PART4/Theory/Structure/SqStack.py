#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
class StackError(Exception):
    pass


class SqStack:
    def __init__(self):
        # 约定最后一个为栈顶
        self._elems = []

    def top(self):
        assert self._elems, StackError('stack is empty!')
        return self._elems[-1]

    def is_empty(self):
        """判断是否为空"""
        return self._elems == []

    def push(self, values):
        """入栈"""
        self._elems.append(values)

    def pop(self):
        """出栈"""
        assert self._elems, StackError('stack is empty!')
        return self._elems.pop()

    def display(self):
        """输出"""
        while not self.is_empty():
            print(self.pop(), end=' ')


if __name__ == '__main__':
    st = SqStack()
    # print(st.top())
    st.push(10)
    print(st.is_empty())
    st.push(30)
    st.display()
