#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import threading
from time import sleep


def music():
    for i in range(5):
        sleep(2)
        print(os.getpid(), 'play music...')


# 创建线程对象
t = threading.Thread(target=music)
t.start()
# 主线程任务
for i in range(3):
    sleep(3)
print(os.getpid(), "播放跳舞吧")
t.join()  # 回收线程
