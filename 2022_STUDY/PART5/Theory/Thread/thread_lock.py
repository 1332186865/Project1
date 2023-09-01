#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
from threading import Thread, Lock

a = b = 0
lock = Lock()


def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d, b = %d" % (a, b))
        lock.release()


t = Thread(target=value)
t.start()
try:
    while True:
        with lock:
            a += 1
            b += 1
            print(a, b)
except KeyboardInterrupt:
    print("End!")
finally:
    t.join()
