#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
from socket import socket

s = socket()
s.bind(('192.168.0.186', 8888))
s.listen(3)

c, addr = s.accept()
print('Connect from:', addr)
data = c.recv(4096)
print(data)

data = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello world!<h1>
"""
c.send(data.encode())
c.close()
s.close()
