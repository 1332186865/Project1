#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
# 手动创建corpus语料库目录，Category_1，Category_2，Category_3,分类目录
import re

for i in range(1, 49):  # 49指文档的数量
    with open(f"./corpus/{i}.txt", encoding='utf-8') as file:  # 循环打开所有文档
        data = file.read().lower()  # 将字母改为小写
        if "community with a shared future" in data:
            pattern_1 = re.compile(r'community with a shared future.{0,10}for', re.S)  # 查找以for为关键词的典型共现
            pattern_2 = re.compile(r'community with a shared future.{0,10}in', re.S)
            answer_1 = pattern_1.findall(data)  # 寻找以for为关键词的典型共现
            answer_2 = pattern_2.findall(data)
            if answer_1:
                with open(f"./Category_1/{i}.txt", "w", encoding="utf-8") as fl:  # 将符合pattern_1规律的文档放在Category_1目录下
                    fl.write(data)
            elif answer_2:
                with open(f"./Category_2/{i}.txt", "w", encoding="utf-8") as fl:
                    fl.write(data)
            else:
                with open(f"./Category_3/{i}.txt", "w", encoding="utf-8") as fl:
                    fl.write(data)
print("Finish!")
