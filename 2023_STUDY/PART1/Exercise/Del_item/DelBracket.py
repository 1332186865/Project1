#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import re


class DelBracket:
    def __init__(self):
        self.orig_folder = "./data/B-Corpus"
        self.dest_folder = "./data/B-Corpus-del"

    def run(self):
        files = [f for f in os.listdir(self.orig_folder) if f.endswith('.txt')]
        for file in files:
            with open(f"{self.orig_folder}/{file}", "r", encoding='utf-8') as f:
                print(f"Working: {self.orig_folder}/{file}")
                data = f.read()
                data = re.sub(r"Introduction\n", '', data)
                data = re.sub(r"\[\d*?]", '', data)
                data = re.sub(r"\(.*?\)", '', data)
                data = re.sub(r"\[.*?]", '', data)
                # data = re.sub(r"\[\d*?]", '', data)
                # data = re.sub(r"\[(i|ii|iii|iv|v|vi|vii|viii|ix|x)]", '', data)
                # data = re.sub(r"\(, ; Singh et al., 2022\)", '', data)
                # data = re.sub(r"\(; Ravaglia, Espley, Henry-Kirk, Andreotti, Ziosi, Hellens, et al., 2013\).", '', data)
                # data = re.sub(r"（BEPS;;）", '', data)
                # data = re.sub(r"\(, ; Singh et al., 2022\)", '', data)
                # data = re.sub(r"\(, ; ; ; \)", '', data)
                # data = re.sub(r"\(, ; ; ; ; \)", '', data)
                # data = re.sub(r"\(, ; ; \)", '', data)
                # data = re.sub(r"\(, ; \)", '', data)
                # data = re.sub(r"\(, Qi et al., 2020; \)", '', data)
                # data = re.sub(r"\(, ; ; ; \)", '', data)
                # data = re.sub(r"\(Li et al., 2020; ; \)", '', data)
                # data = re.sub(r"CV&#x3B1;R", '', data)
                # data = re.sub(r"\(, ; \)", '', data)
                # data = re.sub(r"\(; Jia et al., 2022\)", '', data)
                # data = re.sub(r"\(; Wu et al., 2021\)", '', data)
                # data = re.sub(r"\[, ]", '', data)
                # data = re.sub(r"\(; Wu et al., 2021\)", '', data)
                # data = re.sub(r"\(a; ; \)", '', data)
                # data = re.sub(r"\(\)", '', data)
                # data = re.sub(r"\(, ; ; \)", '', data)
                pattern = re.compile(r'\(.+?\d?\)')  # 定义正则表达式，用于匹配乱码字符
                result = re.findall(pattern, data)
                # for i in result:
                #     if not re.match(r"\([a-zA-Z ]+?\)", i):
                #         re.sub(fr"{i}", "", data)

                with open(f"{self.dest_folder}/{file}", "w", encoding='utf-8') as g:
                    g.write(data)
                print("Done!")
        print("All Done")


if __name__ == '__main__':
    DelBracket().run()