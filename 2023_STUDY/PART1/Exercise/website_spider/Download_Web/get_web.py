#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import random
import time
from time import sleep
import logging
import requests


class Spider:
    """Spider class."""

    def __init__(self):
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/115.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                          "*/*;q=0.8,application/signed-exchange",
                "Cookie": "null; htcatalog=128.148650658352c5b26.23535572; tracker=D1D1D1D1D1; MDPsid=ec3f0100b0d1da3b5fde9331aac28c7c; STICKY=s172",
                "Host": "babel.hathitrust.org",
                "Connection": "close"}
        self.url_list = []
        self.logger = self.log()

    def parse_url(self, title, url):
        """send request to get html and save it."""
        while True:
            self.logger.info(f"{title}, {url}")
            response = requests.get(url, headers=self.headers)
            sleep(random.randint(2, 10))
            file_path = f"web_data/{title}.pdf"
            if response.status_code == 200:
                self.logger.info(f"{title} is downloaded.")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                break

            else:
                self.logger.warning(f"Return Code: {response.status_code}")
                self.logger.warning(response.text)
                time.sleep(random.randint(320, 430))

    def get_url_list(self):
        """get url list from file."""
        # with open("url_list.txt", "r", encoding="UTF-8") as f:
        #     for line in f.readlines():
        #         self.url_list.append(line.strip())

        # self.url_list = ["1 https://babel.hathitrust.org/cgi/imgsrv/download/pdf?id=mdp.39015076618118&attachment=1"
        #                  "&tracker=D1&seq=1"]

        for i in range(578, 600):
            self.url_list.append(f"{i} https://babel.hathitrust.org/cgi/imgsrv/download/pdf?id=mdp.39015076618118&attachment=1&tracker=D1&seq={i}")

    def log(self):
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

    def run(self):
        """run spider."""
        self.get_url_list()
        for url in self.url_list:
            self.parse_url(*url.split(" "))


if __name__ == "__main__":
    Spider().run()