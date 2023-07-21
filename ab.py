
import os
import requests

url = "https://api.abeiyun.com/www/vps.php?cmd=free_vps_init&ie=utf-8"
headers = {
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "no-cache, must-revalidate, max-age=0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5169 MMWEBSDK/20221011 MMWEBID/3263 MicroMessenger/8.0.30.2260(0x28001E3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "accept": "*/*",
    "X-Requested-With": "com.tencent.mm",
    "connection": "close",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.abeiyun.com/",
    "cookie": "session_id=1689563694167071533; laiyunUrl=https://www.abeiyun.com/control/; __root_domain_v=.abeiyun.com; _qddaz=QD.124189516204064; _qdda=3-1.hiz8m; _qddab=3-41ycnt.lk5ibqg7"
}

cookies_str = os.getenv("abck")
if not cookies_str:
    print("请添加cookie")
    exit()

cookies_list = cookies_str.split("\n")

for index, cookies in enumerate(cookies_list):
    headers["Cookie"] = cookies

    response = requests.post(url=url, headers=headers)

    print(f"Response {index+1}:")
    print(response.content.decode("utf-8"))
