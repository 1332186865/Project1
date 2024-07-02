#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import logging
import random
import time
from time import sleep

import requests


class Spider:
    """Spider class."""

    def __init__(self):
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                          "*/*;q=0.8,application/signed-exchange",
                "Cookie": "MDPsid=ab7ad7f56e663c1bad63dbe76c0f843c; STICKY=s189; HT-cookie-banner-seen=true; HT-tracking-cookie-consent=true; HT-marketing-cookie-consent=true; HT-preferences-cookie-consent=true",
                "Host": "babel.hathitrust.org",
                "Connection": "close"}
        self.url_list = []
        self.logger = self.log()
        self.start = 981
        self.end = 1313
        self.id = 'pst.000067504923'
        self.url = (f'https://babel.hathitrust.org/cgi/imgsrv/download/pdf?id={self.id}&attachment=1&tracker'
                    f'=D1&seq=')

    def parse_url(self, title, url):
        """send request to get html and save it."""
        while True:
            self.logger.info(f"{title}, {url}")
            response = requests.get(url, headers=self.headers)
            sleep(random.randint(1, 5))
            file_path = f"web_data/{int(title):0>4d}.pdf"
            if response.status_code == 200:
                self.logger.info(f"{title} is downloaded.")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                break

            else:
                sec = random.randint(250, 360)
                self.logger.warning(f"Return Code: {response.status_code}, Waiting {sec} seconds...")
                # self.logger.warning(response.text)
                time.sleep(sec)

    def get_url_list(self):
        """get url list from file."""
        for i in range(self.start, self.end, 1):
            self.url_list.append(f"{i} {self.url}{i}")

    def log(self):
        """log"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("log_3.log", mode='a', encoding="UTF-8")
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
