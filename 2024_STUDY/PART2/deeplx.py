#  Copyright (c) 2024. Generated by Gu.
#  -*- coding=utf-8 -*-
import sys
import time

import requests

# DeepLX接口列表
deepl_urls = [
        "http://82.157.137.187:1188/translate", "http://123.60.157.70:8085/translate",
        "http://175.178.237.179:1188/translate", "http://117.50.183.46:1188/translate",
        "http://101.43.76.234:1188/translate", "http://104.234.60.178:1188/translate",
        "http://107.175.28.239:1188/translate", "http://148.135.107.108:1188/translate",
        "http://211.227.72.101:1188/translate", "http://194.87.252.161:1188/translate",
        "http://132.145.80.159:1188/translate",
        "https://api.deeplx.org/GEFOIdAQNHPoDGo8se8f6JSPxxDpLveExrACJgMibZ8/translate",
        "https://api.deeplx.org/translate"
        ]

# 测试请求参数
test_data = {
        "text": "Hello, world!",
        "source_lang": "EN",
        "target_lang": "ZH"
        }

# 用来收集可用接口及其响应时间
available_endpoints = []

count = 0
line_count = len(deepl_urls)
# 检测每个接口的可用性和延迟
for url in deepl_urls:
    count += 1
    print("\r", end="")
    print(f"进度: {count / line_count:.2%}: ", "▓" * int(count / line_count * 100 // 2), end="")
    sys.stdout.flush()
    try:
        start_time = time.time()
        response = requests.post(url, json=test_data, timeout=5)
        latency = time.time() - start_time
        # 确保服务真正可用
        if response.status_code == 200 and ('data' in response.json() and len(str(response.json().get("data"))) > 0):
            available_endpoints.append((url, latency))
    except requests.exceptions.RequestException:
        continue  # 忽略错误，只关注可用接口

# 根据延迟时间排序接口
available_endpoints.sort(key=lambda x: x[1])

# 打印界面美化
print("\nAvailable DeepLX Endpoints with Latencies:")
print("-" * 60)
for endpoint, delay in available_endpoints:
    print(f"🚀 ({delay:.2f}s) {endpoint}")
print("-" * 60)

# 打印所有可用的接口，按延迟排序，格式为"DeepLX👌：(count)"
if available_endpoints:
    formatted_endpoints = ", ".join([endpoint[0] for endpoint in available_endpoints])
    print(f"\nDeepLX👌：({len(available_endpoints)}) {formatted_endpoints}\n")
else:
    print("No available endpoints found.\n")
