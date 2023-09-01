#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import struct
from socket import *

ADDR = ('192.168.0.186', 8888)

# 规定数据格式
st = struct.Struct('i32sif')

s = socket(AF_INET, SOCK_DGRAM)

while True:
    try:
        id = int(input('ID:'))
        name = input("name:").encode()
        age = int(input('age:'))
        score = float(input('score:'))
    except ValueError:
        break

    data = st.pack(id, name, age, score)
    s.sendto(data, ADDR)
s.close()
