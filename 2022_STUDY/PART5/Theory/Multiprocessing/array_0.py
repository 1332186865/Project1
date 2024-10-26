#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
from multiprocessing import Process, Array

# 创建共享内存
# 共享内存开辟5个整型列表空间
# shm = Array('i', 5)

# 共享内存初始化数据[1,2,3]
# shm = Array('i', [1, 2, 3])

# 字节串
shm = Array('c', b'hello')


def fun():
    # 共享内存对象可迭代
    for i in shm:
        print(i)
    # 修改共享内存
    shm[0] = b'H'


p = Process(target=fun)
p.start()
p.join()

# 通过va1ue属性访问字节串
print(shm.value)
