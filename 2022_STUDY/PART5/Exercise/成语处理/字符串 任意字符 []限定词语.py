# 根据名词字符串提取需要进一步分析做主语 宾语 状语的部分

import logging
import os
import re


class Finding:
    def __init__(self):
        self.current_file = None
        self.str_dir = r"data/25宾语 判断 字符串.txt"
        self.docx_dir = r"data/24宾语_全_片段.txt"
        self.output_dir = r"data/28宾语_判断动词_片段.txt"
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
        if os.path.exists(self.output_dir):
            os.remove(self.output_dir)
        with open(self.str_dir, 'r', encoding='utf-8') as str_file:
            for word in str_file:
                self.count_word += 1
                self.logger.info(f"正在处理{word.strip()}，目前已处理第{self.count_word}个")
                with open(self.docx_dir, 'r', encoding='utf-8') as docx_file:
                    for line in docx_file:
                        p = re.compile(rf".*?{word.strip()}.*?\[.*?](的|了|吗|之一|外|吧|啊|呢|呵|呀|一般|以后|\n)")
                        line_temp = re.match(pattern=p, string=str(line))
                        if line_temp is not None:
                            self.count += 1
                            self.logger.info(f"正在写入{word.strip()}，目前已写入第{self.count}个")
                            with open(self.output_dir, 'a', encoding='utf-8') as out_file:
                                out_file.write(line)

    def main(self):
        try:
            self.run()
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    Finding().main()
