import logging
import os
import re


class Finding:
    def __init__(self):
        self.current_file = None
        self.str_dir = r"data/25宾语 动作 字符串.txt"
        self.output_dir = r"data/25宾语 动作 字符串_去单.txt"
        self.logger = self.log()
        self.count = 0
        self.count_word = 0

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
        with open(self.str_dir, "r", encoding='utf8') as file:
            for word in file:
                self.count += 1
                if len(word.strip()) > 1:  #
                    with open(self.output_dir, "a", encoding='utf8') as file2:
                        file2.write(word)
                        self.count_word += 1
                        self.logger.info(f"Working: {word.strip()}")
        self.logger.info(f"一共{self.count} 提取{self.count_word}")

    def main(self):
        try:
            self.run()
        except Exception as e:
            self.logger.error(e)

if __name__ == '__main__':
    Finding().main()
