#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random

# 生成5位数的数字验证码
code = "".join(random.choices("0123456789", k=5))

url = f"https://www.shanghairanking.cn/rankings/bcur/2023?__cf_chl_captcha_tk__={code}"

response = requests.get(url)
response.encoding='utf-8'
soup = BeautifulSoup(response.text, "lxml")

universities = []
table = soup.find_all(class_='name-cn')
for item in table[:21]:
    print(item.string)




#     university = {
#         "rank": columns[0].text.strip(),
#         "name": columns[1].text.strip(),
#         "location": columns[2].text.strip(),
#         "type": columns[3].text.strip(),
#         "score": columns[4].text.strip(),
#         "level": columns[5].text.strip()
#     }
#
#     universities.append(university)
#
# for university in universities:
#     print("排名：", university["rank"])
#     print("名称：", university["name"])
#     print("省市：", university["location"])
#     print("类型：", university["type"])
#     print("总分：", university["score"])
#     print("办学层次：", university["level"])
#     print("")