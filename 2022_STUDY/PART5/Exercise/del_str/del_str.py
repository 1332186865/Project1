#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-

with open("11.txt", encoding='utf8') as fl1:
    data = [item[55:] for item in fl1]


data = [i.replace("\\N", " ") for i in data]
with open("ZH.txt", 'w', encoding='utf8') as fl2:
    for item in data:
        fl2.write(item)