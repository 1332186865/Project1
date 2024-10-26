#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import logging
import random
from time import sleep

import requests


class Downloader:
    def __init__(self):
        self.orig_folder = "./web_address/data.tsv"
        self.dest_folder = "./web_orig"
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
        self.country_data = {}
        self.logger = self.log()

    @staticmethod
    def log():
        """log"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("download.log", mode='a', encoding="UTF-8")
        sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(sh)
        logger.info("log init")
        return logger

    def parse_url(self, country: str, url: str) -> None:
        """send request to get html and save it.

        Args:
            country: 标题
            url: 链接
        """
        self.logger.info(f"{country}, {url}")
        response = requests.get(url, headers=self.headers)
        sleep(random.randint(0, 2))
        file_path = f"{self.dest_folder}/{country}-{self.country_data[country]}.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.content.decode())

    def run(self):
        with open(self.orig_folder, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split('\t')
                country, url = data[0], data[3]
                self.country_data[country] = self.country_data.get(country, 0) + 1
                count = 0
                while True:
                    try:
                        if count == 3:
                            raise SystemExit
                        self.parse_url(country, url)
                        count = 0
                        break
                    except Exception as e:
                        self.logger.error(f"Error: {e}")
                        self.logger.error(f"Error URL: {url}")
                        count += 1


if __name__ == '__main__':
    Downloader().run()
