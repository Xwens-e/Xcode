#23/7/24 增加分享和下载任务 默认分享10次
#@xxxc137
#变量 kkpck 抓UID;SESSIONID 多号换行隔开
import requests
import os
import re

cookies = os.environ.get("kkpck").split("\n")
signin_url = "http://newapi.kukupao.top/tuhao/signin?"
lottery_url = "https://m.kukupao.com.cn/member/getblindboxaward"
share_url = "http://newapi.kukupao.top/member/donesharetask?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=night&cryptdata=EbHblWaZGgZD0U6nwYezj9V3zzvU2O3SG3cKZNcxKEOwrl%2BwFrxlq8JN0w1%2FIte%2BM%2FrMNvBO9w5sOAVYENvB29PoEM%2BlnPauVAo02OD3%2BK0je9G%2FMn%2BNkQSv9xxzTs5OevGM1x4lqxreRFFVlGuxEcOR9EZh7WM6SNOcBgsEv7c%3D"
xz_url = "http://newapi.kukupao.top/downloadsuccess?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=white&cryptdata=jj1ZoL5%2FqoGejDaPZQ8%2BHAHcNP8A4Dd%2B87RQnNaN%2BI3zRi%2F3IaEIkvPUjJtWukPa2PNzBCwe66HYJXPHEEU3eih%2FgsGh22uFhw1oVtt6fmVrPYDZkQzpaUSj5UsSzAgiWb7ym85J6clhD%2FE1DB5c4hP2XDSCGXkRgsqz%2FOOMhY2oqOqZl2zbQRzv0Ug1hT3IMVXJvF9vjROyt1ZMUCSXitzl3wMaE16UgRyN1t3OafbbaYrf5ZdFgAxMe3HXhNgjM%2FSZD7fBb6niep6Azpigl8w3u%2B0aSelKcTU90sv1EKzL7M7aUWQbTkXgZXv0p%2F0TCRKYD1faoBOP84ZdSwJucQ%3D%3D"


for cookie in cookies:
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }
print("///////////////////开始签到//////////////////")

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

    print("///////////////////开始分享//////////////////")

    for i in range(10):
        share_response = requests.get(url=share_url, headers=headers)
        if share_response.ok:
            share_result = share_response.content.decode('unicode_escape').replace('\\/', '/')
            print("分享", i+1, ":", share_result)
        else:
            print("分享", i+1, "失败")
    print("/////////////////下载app任务////////////////")
    
    xz_response = requests.get(url=xz_url, headers=headers)
    if lottery_response.ok:
        xz_result = xz_response.content.decode('unicode_escape').replace('\\/', '/')
        print("✅下载app完成:", xz_result)
    else:
        print("❌请求失败")
