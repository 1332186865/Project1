import json

import requests

url = "https://fanyi.baidu.com/basetrans"
data_dict = {
    "query": "如果有空位置，游戏不能结束",
    "from": "zh",
    "to": "en",
    "sign": "289133.35420",
    "token": "a6dbbcd713a85388863dacc0cdc3c513"
    }
headers_dict = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1",
    "Cookie": "BAIDUID=0A56A2723B57B8F4AEEE056D1D4E3890:FG=1; BIDUPSID=09634B3C85E8CC2A6A6A194E2A79F93A; "
              "PSTM=1575051572; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; "
              "BDUSS=k5kOWVRRFBmVUh5NU1QZlYxZ1JXQkR4SDV2QjJPbllCczVqeUtmcVZxVHp"
              "-QWxlRVFBQUFBJCQAAAAAAAAAAAEAAABqcBczamlhX"
              "-ixAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPNv4l3zb-Jdf; "
              "H_PS_PSSID=1423_21082_20697; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1575127780,1575135783; "
              "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1575135802; "
              "from_lang_often=%5B%7B%22value%22%3A%22est%22%2C%22text%22%3A%22%u7231%u6C99%u5C3C%u4E9A%u8BED%22%7D%2C"
              "%7B%22value%22%3A%22cs%22%2C%22text%22%3A%22%u6377%u514B%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C"
              "%22text%22%3A%22%u4E2D%u6587%22%7D%5D; "
              "to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A"
              "%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; "
              "HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; "
              "yjs_js_security_passport=92fcd939ce7b8845e696d1832c93d907288129ac_1575135808_js; "
              "BDSFRCVID=3q-sJeCCxG3jlXJwI7hzbnFY0dQ_1_WOoxuo3J; "
              "H_BDCLCKID_SF=tJuq_II2JCL3fP36q4rM-P_y52T22jPe-4jeaJ5n0-nnhnc1WM6byj"
              "-J2x5X0qFj5N6dox76Bb7WfJARy66jK4JKjH8OqTJP; delPer=0; PSINO=1; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; "
              "H_WISE_SIDS"
              "=136721_138441_138434_128068_137657_135847_136436_120160_138490_137758_137978_132910_137690_131246_132552_137746_131518_118881_118877_118855_118837_118794_136688_107315_136431_138844_137901_136862_138147_138325_138114_136195_124621_137104_133847_138478_138343_137467_137734_131423_138663_137703_138607_110085_127969_138615_131953_137829_138274_127417_138313_136636_138425_138563_138942_138249_138302_138779; rsv_i=d6e9TNJb%2B3qKFQl8TUR%2BTZHvVqSR0wpofuwSqkQaewKiSq6vpJ4oYYAPIrNRiVRuqcIBsOHqnRRCn0DbP237jNis2u6sROs; FEED_SIDS=279036_1201_0; SE_LAUNCH=5%3A26252237_0%3A26252238; __yjsv5_shitong=1.0_7_5d9723b2e9549953a9853d661368336b7ae6_300_1575135783462_111.53.209.103_3a468be1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1575135802; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1575135802 ",
    }

response = requests.post(url, data=data_dict, headers=headers_dict)
print(response)
print(response.content.decode())
r = requests.post(url, data=data_dict, headers=headers_dict)
dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("results =", ret)
