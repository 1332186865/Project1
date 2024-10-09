#  -*- coding=utf-8 -*-
import os
import re
import logging

from bs4 import BeautifulSoup


class Finder:
    def __init__(self):
        self.data_folder = "./orig"
        self.output_folder = "./data"
        self.result_file = ""
        self.data = None
        self.wrong_html = []

        self.log_folder = r"./log"
        self.current_file = None
        self.logger = self.log()

    def log(self):
        """log"""
        current_file_path = os.path.abspath(__file__)
        self.current_file = current_file_path.split("\\")[-1][:-3]
        if not os.path.exists(f"{self.log_folder}/{self.current_file}.log"):
            with open(f"./log/{self.current_file}.log", 'w', encoding='utf8'):
                pass
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

    def main(self):
        html_files = [f for f in os.listdir(self.data_folder) if f.endswith('.html')]
        for html_file in html_files:
            self.result_file = os.path.basename(html_file)[:-5] + ".txt"
            if os.path.exists(f"{self.output_folder}/{self.result_file}"):
                os.remove(f"{self.output_folder}/{self.result_file}")
            with open(f"{self.data_folder}/{html_file}", "r", encoding='utf-8') as f:
                self.logger.info(f"File: {html_file}\t")
                soup = BeautifulSoup(f.read(), 'lxml')
                self.data = None
                try:
                    for tag in soup.find_all('a'):
                        tag.replace_with(tag.get_text().strip())
                    title = soup.find("h1", class_="news-tit").text
                    richtext = soup.find_all("div", class_="richtext")
                    self.data = [richtext[0].get_text("\n", strip=True).replace(u'\xa0', u' ')
                                 .replace(u'\u202f', u' ')]
                    for item in richtext[1:]:
                        self.data += [i.get_text(" ", strip=True).replace(u'\xa0', u' ')
                                      .replace(u'\u202f', u' ') for i in item.find_all("p")]
                    self.logger.info(f"processing: {html_file}")
                except (AttributeError, TypeError) as e:
                    self.logger.warning(e)
                    self.wrong_html.append(html_file[:-5])
                finally:
                    with open(f"{self.output_folder}/{self.result_file}", 'w', encoding='utf-8') as file:
                        write_data = f"{title}\n" + "\n".join(self.data)
                        write_data = re.sub(r" +", " ", write_data)
                        write_data = re.sub(r"\n+", "\n", write_data)
                        file.write(write_data)
                    self.logger.info(f"Done: {html_file}")
        if self.wrong_html:
            self.logger.warning(f"Error html: {"".join(self.wrong_html)}")
        else:
            self.logger.info("No problem. Great!")
        self.logger.info(f"All Done!")


if __name__ == '__main__':
    Finder().main()
