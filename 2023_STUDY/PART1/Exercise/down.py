import requests

# 定义开始和结束的id
start_id = 66900
end_id = 100000

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Cookie": "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218e228aa215d1-0073ac901e573ac8-26001b51-1638720-18e228aa216ca%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2218e228aa215d1-0073ac901e573ac8-26001b51-1638720-18e228aa216ca%22%7D; sajssdk_2015_cross_new_user=1",
        "Dnt": "1",
        "Referer": "https://www.google.com/",
        "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Arch": '"x86"',
        "Sec-Ch-Ua-Bitness": '"64"',
        "Sec-Ch-Ua-Full-Version": '"118.0.5993.118"',
        "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="118.0.5993.118", "Google Chrome";v="118.0.5993.118", '
                                       '"Not=A?Brand";v="99.0.0.0"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Model": '"',
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Ch-Ua-Platform-Version": '"10.0"',
        "Sec-Ch-Ua-Wow64": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

# 创建一个空的列表，用于存储所有数据
data_list = []

# 使用生成器表达式创建一个id的范围，从start_id到end_id（包含）
ids = (id for id in range(start_id, end_id + 1))

# 对每个id进行循环
for id in ids:
    # 构造请求的URL，其中{id}将被当前的id替换
    url = f'https://webapi.fenbi.com/doc/api/publs/{id}'
    # 使用GET方法发送请求，并获取响应
    response = requests.get(url, headers=headers)
    # 从响应中获取'data'字段的数据
    if response.status_code == 200:
        data = response.json()['data']

        #    如果获取的数据为空，则打印一条消息并跳过当前循环
        if data == {}:
            print(f"Empty data for id {id}, skipping...")
            continue

        try:
            # 从数据中提取'name'和'id'字段的值，并尝试将其存储到name和id变量中
            name = data['name']
            id = data['id']
            # 将提取的数据添加到data_frame和all_data中
            data_list.append([id, name])
            print(f"Extract data for id {id}")
            # 如果在尝试提取数据时出现KeyError（即数据中没有'name'或'id'字段），则打印一条错误消息
        except KeyError:
            print(f"Failed to extract data for id {id}")
        except Exception as e:
            print(f"An error occurred while processing id {id}: {str(e)}")

    if response.status_code == 400:
        print(f"Bad request for id {id}")
    if id % 1000 == 0:
        with open(f'{id % 1000}.csv', 'a', encoding='utf-8') as file:
            for i in data_list:
                file.write(f"{i[0]}, {i[1]}, '\n'")

print('完成')
# https://www.fenbi.com/spa/doc-user/file?id=25083
# https://webapi.fenbi.com/doc/api/publs/22144
# https://www.fenbi.com/spa/doc-user/dir/20788
