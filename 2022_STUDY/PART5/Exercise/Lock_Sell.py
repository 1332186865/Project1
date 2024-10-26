#  Copyright (c) 2024. Generated by Gu.
#  -*- coding=utf-8 -*-

# 现在有500张票，存在一个列表中    ["T1",...."T500"]，10个窗口同时卖这500张票    W1-W10
# 使用10个线程模拟这10个窗口，同时卖票，直到所有的票都卖出为止，每出一张票    需要0.1秒，打印表示即可 print("W1----T250")
from threading import Thread, Lock
from time import sleep

lock = Lock()  # 创建锁 # 将票准备好

ticket = ["T%d" % x for x in range(1, 501)]  # 线程函数    w:表示窗口


def sell(w):
    while True:
        sleep(0.1)
        lock.acquire()
        if ticket:
            print("%s\t---\t%s" % (w, ticket.pop(0)))
            lock.release()
        else:
            lock.release()
            break


jobs = []
# 10个线程
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

for item in jobs:
    item.join()
