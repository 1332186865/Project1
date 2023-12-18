#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import logging
import os
import re

from bs4 import BeautifulSoup


class Finder:
    def __init__(self):
        self.data_folder = ""
        self.result_folder = ""
        self.result_folder_rm = ""
        self.result_file = "result.tsv"
        self.all_data = []
        self.web_data = ''
        self.art_path = ''
        self.wrong_article = []
        self.code = ''
        self.article_name = ""
        self.logger = self.log()

    def article(self, data):
        """杂志名"""
        self.code_num(data)
        self.data_folder = f"./{data}"
        self.result_folder = f"./{data}_R"
        self.result_folder_rm = f"./{data}_RB"

    def code_num(self, data):
        self.article_name = data
        if data == "Agricultural and Forest Meteorology":
            self.code = 'F'
        if data == "Agricultural Water Management":
            self.code = 'C'
        if data == "Postharvest Biology and Technology":
            self.code = 'B'
        if data == "The Crop Journal":
            self.code = 'D'

    @staticmethod
    def remove_garbled_characters(text):
        text = re.sub(r"&amp;nbsp;×&amp;nbsp;", " x ", text)
        text = re.sub(r"&nbsp;", " ", text)
        # text = re.sub(r'<sup.*?</sup>', " ", text)
        text = re.sub(r'=E2=88=92 1', "-1", text)
        text = re.sub(r'=E2=80=99', "'", text)
        text = re.sub(r'=E2=80=93', "-", text)
        text = re.sub(r'=C3=A1', "a", text)
        text = re.sub(r'=..=..=..', "", text)
        text = re.sub(r'=..=..', "", text)
        text = re.sub(r'=\n', "", text)
        pattern = re.compile(r'[^\x00-\x7F]+')  # 定义正则表达式，用于匹配乱码字符
        result = re.sub(pattern, ' ', text, re.S)  # 使用空字符串替换乱码字符
        return result

    @staticmethod
    def remove_a(item):
        for j in item:
            if j.name == "a":
                j.decompose()
        temp = item.text
        temp = re.sub(r"( ,)+", "", temp)
        temp = re.sub(r" \(\)", "", temp)
        temp = re.sub(r" \[]", "", temp)
        temp = re.sub(r" \[,+]", "", temp)
        temp = re.sub(r"\((, )+\)", "", temp)
        temp = re.sub(r"\((,)+\)", "", temp)
        temp = re.sub(r"\((; )+\)", "", temp)
        temp = re.sub(r"\((;)+\)", "", temp)
        temp = re.sub(r"\[\d*?]", '', temp)
        temp = re.sub(r"\(e.g., (; )*\)", "", temp)
        temp = re.sub(r"\(i.e., (; )*\)", "", temp)
        return temp

    @staticmethod
    def temp_save(text):
        with open("./1.mhtml", "w", encoding="utf-8") as f:
            f.write(text)

    def introduction(self, data):
        """Introduction finding"""
        intro = None
        if self.code == "B":
            intro = data.find('section', id='3D"sec0005"')
        elif self.code == "C":
            intro = data.find('section', id='3D"sec0005"')
        elif self.code == "D":
            intro = data.find('section', id='3D"s0005"')  # 需要修改Introduction的标签 顾
        elif self.code == "F":
            intro = data.find('section', id='3D"sec0001"')  # 需要修改Introduction的标签 东阳1
            if intro is None:
                intro = data.find('section', id='3D"sec1"')  # 需要修改Introduction的标签 东阳2
            if intro is None:
                intro = data.find('section', id='3D"sec0002"')  # 需要修改Introduction的标签 东阳3
        return intro

    def method(self):
        if os.path.exists(f"{self.result_folder}/{self.result_file}"):
            os.remove(f"{self.result_folder}/{self.result_file}")
        html_files = [f for f in os.listdir(self.data_folder) if f.endswith('.mhtml')]
        for html_file in html_files:
            with open(f"{self.data_folder}/{html_file}", "r", encoding='utf-8') as f:
                orig_data = self.remove_garbled_characters(f.read())
                self.logger.info(f"File: {self.article_name} {html_file}\t")
                data = BeautifulSoup(orig_data, 'lxml')
                self.web_data = ''
                temp = data.find("div", '3D"text-xs"').text
                current_year = re.search(r"20\d\d", temp).group()[2:]
                self.art_path = f"{self.code}{current_year}-{html_file[:-6]}"

                try:
                    intro = self.introduction(data)
                    # self.web_data += "Introduction" + "\n"
                    for item in intro:
                        if item.name == "div":
                            for i in intro.div.find_all("p"):
                                self.web_data += self.remove_a(i) + "\n"
                        elif item.name == "p":
                            self.web_data += self.remove_a(item) + "\n"
                        elif item.name == "section":
                            for j in item:
                                if j.name == "p":
                                    self.web_data += self.remove_a(j) + "\n"

                    names = ''
                    author_group = []
                    author = data.find("div", id='3D"author-group"')
                    for item in author:
                        if item.name == "button" or item.name == "a":
                            author_group += item
                    for item in author_group:
                        name = item.text
                        names += name + ','

                    institute = data.find("dl", class_='3D"affiliation"').dd.text
                    institute_f = institute.split(", ")[:-1]
                    country = institute.split(", ")[-1]
                    self.all_data.append([self.art_path, names, ','.join(institute_f), country])
                    self.logger.info(f"      {self.article_name} {self.art_path}")

                except (AttributeError, TypeError) as e:
                    self.temp_save(orig_data)
                    self.logger.warning(e)
                    self.all_data.append([self.art_path, "", "", ""])
                    self.wrong_article.append(html_file[:-6])
                finally:
                    article_path = f'{self.result_folder}/{self.art_path}.txt'
                    with open(article_path, 'w', encoding='utf-8') as file:
                        file.write(self.web_data)
                    self.logger.info("Done!")
        with open(f'{self.result_folder}/{self.result_file}', 'a', encoding='utf-8') as f:
            for item in self.all_data:
                f.write(item[0] + '\t' + item[1] + '\t' + item[2] + '\t' + item[3] + '\n')
        if self.wrong_article:
            self.logger.warning(f"存在问题的文件: {self.wrong_article}")
            # self.logger.warning("笑死，没点 Show more 吧")
            # self.logger.warning("还是手太快Introduction没加载出来")
            # self.logger.warning("小概率文章本来就有问题")
        else:
            self.logger.info("No problem. Great!")
        self.logger.info(f"All Done: {self.article_name} Part 1")

    def rm_bracket(self):
        files = [f for f in os.listdir(self.result_folder) if f.endswith('.txt')]
        for file in files:
            with open(f"{self.result_folder}/{file}", "r", encoding='utf-8') as f:
                self.logger.info(f"Working: {self.result_folder}/{file}")
                data = f.read()
                data = re.sub(r" \[\d*?]", '', data)
                data = re.sub(r" \(.*?\)", '', data)
                data = re.sub(r" \[.*?]", '', data)
                with open(f"{self.result_folder_rm}/{file}", "w", encoding='utf-8') as g:
                    g.write(data)
                self.logger.info("Done!")
        self.logger.info(f"All Done: {self.article_name} Part 2")

    @staticmethod
    def log():
        """log"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("log.log", mode='a', encoding="UTF-8")
        sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(sh)
        logger.info("log init")
        return logger

    def main(self):
        data_list = ["Agricultural and Forest Meteorology", "Agricultural Water Management",
                     "Postharvest Biology and Technology", "The Crop Journal"]
        for item in data_list:
            self.article(item)
            self.method()
            self.rm_bracket()


if __name__ == '__main__':
    Finder().main()
