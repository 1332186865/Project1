# 根据名词字符串提取需要进一步分析做主语 宾语 状语的部分

import logging
import os
import re


class Finding:
    def __init__(self):
        self.docx_dir = r"data/65补语_全_片段_去框开头的单独成段.txt"
        self.output_dir = r"data/66补语_全_片段_去框开头和单独成段.txt"
        self.logger = self.log()
        self.count = 0
        self.current_file = ""

    def log(self):
        """log"""
        current_file_path = os.path.abspath(__file__)
        self.current_file = current_file_path.split("\\")[-1][:-3]
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f"./log/{self.current_file}.log", mode='a', encoding="UTF-8")
        sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(sh)
        logger.info("log init")
        return logger

    def run(self):
        if os.path.exists(self.output_dir):
            os.remove(self.output_dir)
        with open(self.docx_dir, 'r', encoding='utf-8') as docx_file:
            for line in docx_file:
                line_temp = re.match(rf"^\[.*?].*?\n", str(line))
                if line_temp is None:
                    self.count += 1
                    self.logger.info(f"正在写入{line.strip()}，目前已写入第{self.count}个")
                    with open(self.output_dir, 'a', encoding='utf-8') as out_file:
                        out_file.write(line)

    def main(self):
        try:
            self.run()
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    Finding().main()
