import requests

session = requests.session()
post_url = "http://www.renren.com/Login"
post_data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

# 模拟登陆三种方法
# method 1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
session.post(post_url, data=post_data, headers=headers)
r = session.get("http://www.renren.com/327550029/profile", headers=headers)

# method 2
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Cookie": "BIDUPSID=4AFE32F37248CDD21FB72371DF09F01D; PSTM=1637836440; BAIDUID=4AFE32F37248CDD23E52CCF87858C0E5:FG=1; BD_UPN=12314753; ORIGIN=2; ISSW=1; ISSW=1; BAIDUID_BFESS=4AFE32F37248CDD23E52CCF87858C0E5:FG=1; BD_HOME=1; H_PS_PSSID=34447_35104_31660_34584_34518_35245_34606_35329_35323_26350_35210_22160; BA_HECTOR=242h05a10g250k0gb61grb0hh0q"}
r = requests.get("http://www.renren.com/327550029/profile", headers=headers)

# method 3
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
cookies = "BIDUPSID=4AFE32F37248CDD21FB72371DF09F01D; PSTM=1637836440; BAIDUID=4AFE32F37248CDD23E52CCF87858C0E5:FG=1; BD_UPN=12314753; ORIGIN=2; ISSW=1; ISSW=1; BAIDUID_BFESS=4AFE32F37248CDD23E52CCF87858C0E5:FG=1; BD_HOME=1; H_PS_PSSID=34447_35104_31660_34584_34518_35245_34606_35329_35323_26350_35210_22160; BA_HECTOR=242h05a10g250k0gb61grb0hh0q"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
r = requests.get("http://www.renren.com/327550029/profile", headers=headers, cookies=cookies)

with open("renren1.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
