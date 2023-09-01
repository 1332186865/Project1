#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
from time import sleep

print("===============")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed!")
elif pid == 0:
    print("Child process.")
    print('a = %d' % a)
    a = 10000
else:
    sleep(1)
    print("Parent process")
    print('a = %d' % a)

# print("Fork test over!")
print("All a = %d" % a)
