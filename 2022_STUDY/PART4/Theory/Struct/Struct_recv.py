#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import struct
from socket import *

ADDR = ('192.168.0.186', 8888)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

st = struct.Struct('i32sif')
f = open('student.txt', 'w')
while True:
    data, addr = s.recvfrom(1024)
    # 数据解析
    data = st.unpack(data)
    info = "%d %s %d %.2f\n" % (data[0], data[1].decode(), data[2], data[3])
    f.write(info)
    print(info)

s.close()
