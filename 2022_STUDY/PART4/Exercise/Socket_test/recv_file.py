#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
from socket import socket

s = socket()
s.bind(('0.0.0.0', 8888))
# s.bind(('192.168.0.186', 28888))  # 接收端地址
s.listen(5)

c, addr = s.accept()
print('Connect from:', addr)

f = open('picture.jpg', 'wb')

# 接收内容写入文件
while True:
    data = c.recv(1024)  # 字节串
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
