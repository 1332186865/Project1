#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
from threading import Thread, Event
from time import sleep

s = None
e = Event()


def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    sleep(1)
    e.set()


t = Thread(target=杨子荣)
t.start()
print("说对口令就是自己人")
e.wait()
print(s)

if s == "天王盖地虎":
    sleep(1)
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人")
else:
    print("打死他...")
t.join()
