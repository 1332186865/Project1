import logging
import os
import re


class Judgement:
    def __init__(self):
        self.current_file = None
        self.str_dir = r"data/7动词字符串（位置关系）.txt"
        self.docx_dir = r"data/9包含目标动词的语料.txt"
        self.output1_dir = r"data/10做主语.txt"
        self.output2_dir = r"data/10做宾语.txt"
        self.logger = self.log()
        self.first = 0
        self.end = 0
        self.count = 0

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

    @staticmethod
    def write_file(file_dir, data):
        with open(file_dir, 'a', encoding='utf-8') as file:
            file.write(data)

    def run(self):
        with open(self.docx_dir, 'r', encoding='utf-8') as docx_file:
            for line in docx_file:
                self.count += 1
                line_temp = re.sub(r'"', "", line)
                line_temp = re.sub(r'\[.*?]', "[]", line_temp)
                with open(self.str_dir, 'r', encoding='utf-8') as word_file:
                    for word in word_file:
                        data = word.strip()
                        try:
                            if data in line_temp:
                                # self.logger.info(data)
                                if line.index(data) > line.index("["):
                                    self.logger.info(data)
                                    self.logger.info(f"Working on {line.strip()} 动词在后 {self.count}/18458")
                                    self.write_file(self.output1_dir, line)
                                    self.end += 1
                                    continue
                                elif line.index(data) < line.index("["):
                                    self.logger.info(data)
                                    self.logger.info(f"Working on {line.strip()} 动词在前 {self.count}/18458")
                                    self.write_file(self.output2_dir, line)
                                    self.first += 1
                                    continue
                        except Exception as e:
                            self.logger.warning(f"{e}")
                            self.logger.warning(f"{data} {line}")

        self.logger.info(f"共{self.count}，动词在前{self.end}， 动词在后{self.first}")


if __name__ == '__main__':
    Judgement().run()
