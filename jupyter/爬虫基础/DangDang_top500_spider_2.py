import json
import re

import requests


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('dangdang.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()
    str_item = str(item)


def func2(page):
    url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?class="name".*?title="(.*?)">.*?class="star".*?target="_blank">(.*?)</a>.*?class="tuijian">(.*?)<.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="price_n">&yen;(.*?)</span>.*?class="price_r">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    print(items)
    return items


if __name__ == '__main__':
    for i in range(1, 26):
        func2(i)
