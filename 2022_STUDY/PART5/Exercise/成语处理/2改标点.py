# 删除标点
import logging
import os
import re
import sys


class Finding:
    def __init__(self):
        self.docx_dir = r"data/72主语 全 去来源.txt"
        self.output_dir = r"data/73主语 全 改标点.txt"
        self.logger = self.log()
        self.count = 0
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
        if os.path.exists(self.output_dir):
            os.remove(self.output_dir)
        line_count = self.count_lines(self.docx_dir)
        with open(rf"{self.docx_dir}", 'r', encoding='utf-8') as docx_file:
            for line in docx_file:
                self.count += 1
                print("\r", end="")
                print(f"进度: {self.count / line_count:.2%}: ", "▓" * int(self.count / line_count * 100 // 2), end="")
                sys.stdout.flush()
                line_first = re.sub(r"：“", "。", line)
                line_first = re.sub(r":“", "。", line_first)
                line_first = re.sub(r"。”", "。", line_first)
                line_first = re.sub(r"\.”", "。", line_first)
                line_first = re.sub(r"，“", "。", line_first)
                line_first = re.sub(r",“", "。", line_first)
                line_first = re.sub(r",”", "。", line_first)
                line_first = re.sub(r"，”", "。", line_first)
                line_first = re.sub(r"？”", "。", line_first)
                line_first = re.sub(r"\?”", "。", line_first)
                line_first = re.sub(r"[?？;:：；,，！! ]", "。", line_first)
                line_first = re.sub("\n", "\n。", line_first)
                line_first = re.sub("。。", "。", line_first)
                with open(rf"{self.output_dir}", 'a', encoding="utf8") as write_file:
                    write_file.write(line_first)

    def main(self):
        try:
            self.run()
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    Finding().main()
