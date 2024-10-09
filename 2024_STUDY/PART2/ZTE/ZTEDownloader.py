#  -*- coding=utf-8 -*-
import logging
import os
import random
import re
from time import sleep

import requests


class Downloader:
    def __init__(self):
        self.current_file = None
        self.URL = r"./URL.txt"
        self.data_folder = r'./orig'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control": "max-age=0",
            "Cookie": "",
            "If-None-Match": "1fbb4-620bee35bbfbb",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Ch-Ua-Wow64": "?0",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

        self.log_folder = r"./log"
        self.current_file = None
        self.logger = self.log()

    def get_cookie(self):
        """get new cookie"""
        with open("./cookie.txt", "r", encoding='utf-8') as file:
            data = file.read().strip()
            self.headers['Cookie'] = data

    def download(self):
        with open(f"{self.URL}", "r", encoding='utf-8') as file:
            for line in file:
                title = re.search(r"news/(.*?)\.html", line).group(1)
                url = line.strip()
                count = 0
                while True:
                    try:
                        if count == 3:
                            raise SystemExit
                        self.parse_url(title, url)
                        count = 0
                        break
                    except Exception as e:
                        self.logger.error(f"Error: {e}")
                        self.logger.error(f"Error URL: {url}")
                        count += 1

        self.logger.info(f"Finish Download: {title}")
        sleep(random.randint(5, 10))

    @staticmethod
    def remove_garbled_characters(text):
        text = re.sub(r" ", "", text)
        text = re.sub(r"/", "", text)
        text = re.sub(r":", "_", text)
        text = re.sub(r"-", "_", text)
        result = re.sub(r" \| ", "_", text)
        return result

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

    def parse_url(self, title, url):
        """send request to get html and save it."""
        while True:
            self.logger.info(f"Downloading: {title}")
            self.get_cookie()
            title = self.remove_garbled_characters(title)
            response = requests.get(url, headers=self.headers)
            file_path = f"{self.data_folder}/{title}.html"
            if response.status_code == 200:
                self.logger.info(f"{title} is downloaded.")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                sleep(random.randint(3, 10))
                break
            else:
                self.logger.warning(f"Return Code: {response.status_code}")
                self.logger.warning(f"Need to deal with challenge!")
                self.logger.warning(url)
                self.logger.warning("Please refresh cookie")
                # self.logger.warning(response.text)
                sleep(random.randint(5, 15))
                input("Waiting...")

    def main(self):
        """main framework"""
        self.download()


if __name__ == '__main__':
    Downloader().main()
