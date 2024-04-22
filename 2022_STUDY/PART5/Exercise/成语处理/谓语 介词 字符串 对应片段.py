
import logging
import os
import re


class Finding:
    def __init__(self):
        self.current_file = None
        self.str_dir = r"data/25宾语 介词字符串去框.txt"1
        self.docx_dir = r"data/24宾语_全_片段.txt"1
        self.output_dir = r"data/27宾语_介宾分开_片段.txt"1
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
                        line_temp = re.match(rf"{word.strip()}.*?的\[", str(line))1
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