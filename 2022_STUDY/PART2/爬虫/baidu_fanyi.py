#  Copyright (c) 2022. Generated by Gu.
#  百度增加反爬，此代码仅供参考
import json

import requests


class BaiduFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.Lang_detect_url = "http://fanyi.baidu.com/langdetect"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36"}
        self.cookie = {"BIDUPSID": "B5C541CFEC8E2B2F3124DCC0E06075A7", "PSTM": "1641461556",
                       "BAIDUID": "B5C541CFEC8E2B2F6585EB90EF3B8563:F:=1",
                       "BDUSS": "zU1WTlJTnFQbGxQWXRzMmtBTmpQZ0hJZEdiZ3lla2NLZmV3OENHR351WGVjUDVoRVFBQUFBJCQAAAAAAAAAAAEAAADDma1ixq7I9Lih1MY4ODgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN7j1mHe49Zhd",
                       "BDUSS_BFESS": "zU1WTlJTnFQbGxQWXRzMmtBTmpQZ0hJZEdiZ3lla2NLZmV3OENHR351WGVjUDVoRVFBQUFBJCQAAAAAAAAAAAEAAADDma1ixq7I9Lih1MY4ODgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN7j1mHe49Zhd",
                       "H_PS_PSSID": "35105_31660_35489_34584_35490_35802_35796_35319_26350_35746",
                       "BAIDUID_BFESS": "B5C541CFEC8E2B2F6585EB90EF3B8563:FG=1",
                       "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1642909055,1643982077", "REALTIME_TRANS_SWITCH": "1",
                       "FANYI_WORD_SWITCH": "1", "HISTORY_SWITCH": "1", "SOUND_SPD_SWITCH": "1",
                       "SOUND_PREFER_SWITCH": "1", "APPGUIDE_10_0_2": "1",
                       "Hm_lvt_afd111fa62852d1f37001d1f980b6800": "1643982084",
                       "Hm_lpvt_afd111fa62852d1f37001d1f980b6800": "1643982084",
                       "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1643982084"}

    def parse_url(self, url, data):  # 发送POST请求，获取响应
        response = requests.post(url, data=data, headers=self.headers, cookies=self.cookie)
        print(response.content.decode())
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("results is :", ret)

    def run(self):  # 实现主要逻辑
        # 1,获取语言类型
        # 1.1准备post的url地址, post_data
        lang_detect_data = {"query": self.trans_str}
        # 1.2发送POST请求，获取响应
        # 1.3 提取语言类型
        lang = self.parse_url(self.Lang_detect_url, lang_detect_data)["lan"]
        # 2.准备post的数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else \
            {"query": self.trans_str, "from": "en", "to": "zh"}
        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4,提取翻译的结果
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_strs = "今天风很大"
    baidu_fanyi = BaiduFanyi(trans_strs)
    baidu_fanyi.run()
