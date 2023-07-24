#23/7/22
#@xxxc137
import os
import requests

# 设置请求的URL和Headers
url = "http://www.ymg.one/wp-admin/admin-ajax.php?action=user_qiandao&ie=utf-8"
headers = {
    "Connection": 'keep-alive',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cache-Control": 'no-cache, must-revalidate, max-age=0',
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
    "accept": "*/*",
    "connection": "Keep-Alive",
    "Accept-Encoding": "gzip,deflate"
}

cookies_str = os.getenv("ymgck")
if not cookies_str:
    print("请添加cookie")
    exit()

cookies_list = cookies_str.split("\n")

print("///////////////签到开始///////////////")

for index, cookies in enumerate(cookies_list):
    cookies = {
        "wordpress_logged_in_bad61921bfed873fb111d18c00eb5704": cookies
    }

    response = requests.post(url=url, headers=headers, cookies=cookies)
    json_response = response.json()

    if "msg" in json_response:
        if json_response["msg"] == "\u7b7e\u5230\u6210\u529f\uff0c\u8d60\u90010.5\u94bb\u77f3":
            print("🎉签到成功，获得0.5个钻石")
        elif json_response["msg"] == "\u4eca\u65e5\u5df2\u7b7e\u5230\uff0c\u8bf7\u660e\u65e5\u518d\u6765":
            print("📣已经签到过了")
        elif json_response["msg"] == "\u8bf7\u767b\u5f55\u540e\u7b7e\u5230":
            print("❌cookie已过期")
    else:
        print("❌请求失败")
