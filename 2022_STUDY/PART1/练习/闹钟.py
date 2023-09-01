import time


def alarm():
    h = int(input("请输入小时："))
    m = int(input("请输入分钟："))
    while True:
        ct = time.localtime()
        if (h, m) == ct[3:5]:
            print("\n时间到...")
            return
        print("\r%02s:%02s:%02s" % ct[3:6], end="")
        time.sleep(1)


alarm()
