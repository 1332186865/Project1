# 根据名词字符串提取需要进一步分析做主语 宾语 状语的部分

import logging
import os
import re
import sys


class Finding:
    def __init__(self):
        self.str_dir = r"data/状语/源文件"
        self.docx_dir = r"data/状语/100语料.txt"
        self.output_dir = r"data/状语/输出文件"
        self.logger = self.log()
        self.count = 0
        self.count_word = 0
        self.count_file = 0
        self.current_file = ""

    def log(self):
        """log"""
        current_file_path = os.path.abspath(__file__)
        self.current_file = current_file_path.split("\\")[-1][:-3]
        if os.path.exists(f"./log/{self.current_file}.log"):
            os.remove(f"./log/{self.current_file}.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f"./log/{self.current_file}.log", mode='a', encoding="UTF-8")
        # sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        # sh.setFormatter(formatter)
        logger.addHandler(fh)
        # logger.addHandler(sh)
        logger.info("log init")
        return logger

    @staticmethod
    def count_lines(filename):
        count = 0
        with open(filename, 'r', encoding='utf8') as file:
            for _ in file:
                count += 1
        return count

    def run(self):
        file_list = [f for f in os.listdir(self.str_dir) if f.endswith('.txt')]
        for file in file_list:
            self.count_file += 1
            if os.path.exists(f"{self.str_dir}/{file[:-4]}片段.txt"):
                os.remove(f"{self.str_dir}/{file[:-4]}片段.txt")
            line_count = self.count_lines(f"{self.str_dir}/{file}")
            with open(f"{self.str_dir}/{file}", 'r', encoding='utf-8') as str_file:
                for word in str_file:
                    self.count_word += 1
                    self.logger.info(f"正在处理{word.strip()}，目前已处理第{self.count_word}个")
                    print("\r", end="")
                    print(f"文件{self.count_file} 进度: {self.count_word / line_count:.2%}: ",
                          "▓" * int(self.count_word / line_count * 100 // 2), end="")
                    sys.stdout.flush()
                    with open(self.docx_dir, 'r', encoding='utf-8') as docx_file:
                        for line in docx_file:
                            line_temp = re.sub("]地", "]", line)
                            if fr"]{word.strip()}" in line_temp:
                                self.count += 1
                                self.logger.info(f"正在写入{line.strip()}，目前已写入第{self.count}个")
                                with open(f"{self.str_dir}/{file[:-4]}片段.txt", 'a', encoding='utf-8') as out_file:
                                    out_file.write(line)
            self.count_word = 0
            print("\n")

    def main(self):
        try:
            self.run()
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    Finding().run()
