#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import random
import re
from time import sleep

import requests
import unicodedata
from bs4 import BeautifulSoup

from tsv_to_xlsx import TsvToXlsx


class Spider:
    def __init__(self):
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
        self.path = r'./'
        self.TsvToXlsx = TsvToXlsx(self.path + 'African_website/tsv', self.path + 'African_website/xlsx')

    @staticmethod
    def get_newspapers_indexes():
        """
        Get all the African newspapers indexes.
        """
        data = BeautifulSoup(open('African Newspapers index.html', 'r', encoding='utf-8'), 'lxml')
        web_data = []
        try:
            for item in data.find_all('li'):
                web_data.append([item.a.text, item.a['href']])
        except AttributeError:
            with open('African newspapers index.tsv', 'w', encoding='utf-8') as f:
                for item in web_data:
                    f.write(item[0] + '\t' + item[1] + '\n')
            raise SystemExit

    def parse_url(self, title: str, url: str) -> None:
        """send request to get html and save it.

        Args:
            title: 标题
            url: 链接
        """
        print(title, url)
        response = requests.get(url, headers=self.headers)
        sleep(random.randint(0, 2))
        file_path = f"orig_web_data/{title}.html"
        with open(file_path, "w", encoding="UTF-8") as f:
            f.write(response.content.decode())

    def get_newspapers_websites(self):
        with open('African newspapers index.tsv', 'r', encoding='utf-8') as f:
            for line in f:
                self.parse_url(*line.strip().split('\t'))

    @staticmethod
    def list_dir(path):
        """
        Get all the files in a directory.
        """
        temp = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                temp.append([f, os.path.join(path, f)])
        return temp

    @staticmethod
    def find_p(item):
        """judge p is in the item or not."""
        if item.p:
            temp = item.p.text
        else:
            temp = ''
        return temp

    @staticmethod
    def remove_garbled_characters(text):
        """Remove garbled characters."""
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

    def save_newspapers_sites(self):
        """
        Get all the African newspapers indexes.
        """
        temp = self.list_dir(self.path + r'orig_web_data/')
        for title, path in temp:
            print("\033[1;37;40m正在操作:", title, path)
            file = open(path, 'r', encoding='utf-8').read()
            file = unicodedata.normalize('NFKD', file)
            file = self.remove_garbled_characters(file)
            data = BeautifulSoup(file, 'lxml')
            web_data = []
            try:
                aa = data.find_all('li')
                for item in aa:
                    if item.find('h3'):
                        if item.h3.a:
                            web_data.append([item.h3.a.text, item.h3.a['href'], self.find_p(item)])
                    elif item.find('h4'):
                        if item.h4.a:
                            web_data.append([item.h4.a.text, item.h4.a['href'], self.find_p(item)])

            except AttributeError as e:
                print("\033[1;31;40mError:", e)
            finally:
                title = title[:-5]
                with open(f'./African_website/tsv/{title}.tsv', 'w+', encoding='utf-8') as f:
                    # f.write('Title\tURL\tDescription\n')
                    for item in web_data:
                        temp = item[0] + '\t' + item[1] + '\n'
                        # temp = item[0] + '\t' + item[1] + '\t' + item[2] + '\n'
                        f.write(temp)

    def main(self):
        while True:
            temp = int(input('请输入命令:'
                             '\n1. 爬取非洲国家总索引\n2. 下载国家对应网页\n3. 爬取网站链接\n4. TSV转XLSX\n0. 退出程序\n'))
            match temp:
                case 1:
                    self.get_newspapers_indexes()
                case 2:
                    self.get_newspapers_websites()
                case 3:
                    self.save_newspapers_sites()
                case 4:
                    self.TsvToXlsx.tsv_to_xlsx()
                case 0:
                    raise SystemExit


if __name__ == '__main__':
    Spider().main()
