#23/7/23
#@xxxc137
#变量 kkpck 抓UID;SESSIONID 多号换行隔开
import requests
import os

cookies = os.environ.get("kkpck").split("\n")
signin_url = "http://newapi.kukupao.top/tuhao/signin?"
lottery_url = "https://m.kukupao.com.cn/member/getblindboxaward"

print("///////////////////开始签到//////////////////")

for cookie in cookies:
    headers = {
        "Connection": 'keep-alive',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cache-Control": 'no-cache, must-revalidate, max-age=0',
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
        "accept": "*/*",
        "connection": "Keep-Alive",
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }

    response = requests.post(url=signin_url, headers=headers)
    if response.ok:
        data = response.json()
        msg = data.get("msg")

        if msg == "\u4eca\u65e5\u5df2\u7b7e\u5230":
            print("꯭🎈꯭已꯭经꯭签꯭到꯭过꯭了꯭")
        elif msg == "":
            print("꯭🎉꯭签꯭到꯭成꯭功꯭")
        elif msg == "\u7528\u6237\u9a8c\u8bc1\u5931\u8d25\uff0c\u8bf7\u91cd\u65b0\u767b\u9646":
            print("꯭❌꯭c꯭o꯭o꯭k꯭i꯭e꯭已꯭过꯭期꯭")
    else:
        print("请求失败")

    print("///////////////////开始抽奖//////////////////")
    
    lottery_response = requests.get(url=lottery_url, headers=headers)
    if lottery_response.ok:
        lottery_result = lottery_response.content.decode('unicode_escape').replace('\\/', '/')
        print("抽奖结果:", lottery_result)
    else:
        print("抽奖请求失败")
