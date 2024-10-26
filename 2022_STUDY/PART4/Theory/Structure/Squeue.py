#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
class QueueError(Exception):
    pass


class Squeue:
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []

    def enqueue(self, value):
        self._elem.append(value)

    def dequeue(self):
        assert self._elem, QueueError('Queue is empty')
        return self._elem.pop(0)

    def display(self):
        while not self.is_empty():
            print(self.dequeue(), end=' ')


if __name__ == '__main__':
    sq = Squeue()
    sq.enqueue(10)
    sq.enqueue(30)
    sq.enqueue(50)
    print(sq.dequeue())
    sq.display()
