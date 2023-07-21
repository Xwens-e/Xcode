#23/7/17
#@xxxc137
import os
import requests

url = "https://www.wobbt.com/wp-admin/admin-ajax.php?action=user_checkin&ie=utf-8"
headers = {
    "Connection": 'keep-alive',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cache-Control": 'no-cache, must-revalidate, max-age=0',
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
    "accept": "*/*",
    "connection": "Keep-Alive",
    "Accept-Encoding": "gzip,deflate"
}

cookies_str = os.getenv("dpck")
if not cookies_str:
    print("请添加cookie")
    exit()

cookies_list = cookies_str.split("\n")

for index, cookies in enumerate(cookies_list):
    cookies = {
        "wordpress_logged_in_feec45d99d992016e502ed64af77bfb3": cookies
    }

    response = requests.post(url=url, headers=headers, cookies=cookies)
    json_response = response.json()

if "msg" in json_response:
    if json_response["msg"] == "\u7b7e\u5230\u6210\u529f\uff01\u79ef\u5206":
        print("🎉签到成功，+30积分")
        response_data = json_response["data"].encode("utf-8").decode("unicode_escape")
        print(response_data)
    elif json_response["msg"] == "\u4eca\u65e5\u5df2\u7b7e\u5230":
        print("📣已经签到过了")
    elif json_response["msg"] == "0":
        print("❌cookie已过期")
else:
    print("❌请求失败")