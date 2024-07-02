#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os

data = []
files = [f for f in os.listdir("./Zheng He") if f.endswith('.txt')]
for item in files:
    temp = item[:-4].split("-")
    data.append(temp)
with open("data.tsv", "w", encoding="utf-8") as file:
    for i in data:
        file.write(f"{i[0]}\t{i[1]}\t{i[2]}\t{'20'+i[3]}\n")