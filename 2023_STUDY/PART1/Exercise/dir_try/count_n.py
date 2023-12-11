#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import re


class Finder:
    def __init__(self):
        self.data_folder = "./data"
        self.result_file = "result.tsv"
        self.all_data = []

    def main(self):
        temp = [f for f in os.listdir(self.data_folder) if f.endswith('.txt')]
        for item in temp:
            title = item.split('.')[0][7:]
            with open("./data/" + item, 'r', encoding='ansi') as f:
                data = f.read()
                num = len(re.findall("\n", data))
                self.all_data.append([title, num])

        with open(f"./{self.result_file}", "w", encoding="utf-8") as fl:
            for item in self.all_data:
                fl.write(f"{item[0]}\t{item[1]}\n")


if __name__ == '__main__':
    Finder().main()