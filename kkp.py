#23/7/28 任务：签到、分享、抽奖、下载游戏得豆
#@xxxc137
#变量 kkpck 抓UID;SESSIONID 多号换行隔开
import requests
import json
import os
import re
from bs4 import BeautifulSoup

cookies = os.environ.get("kkpck").split("\n")
signin_url = "http://newapi.kukupao.top/tuhao/signin?"
lottery_url = "https://m.kukupao.com.cn/member/getblindboxaward"
share_url = "http://newapi.kukupao.top/member/donesharetask?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=night&cryptdata=EbHblWaZGgZD0U6nwYezj9V3zzvU2O3SG3cKZNcxKEOwrl%2BwFrxlq8JN0w1%2FIte%2BM%2FrMNvBO9w5sOAVYENvB29PoEM%2BlnPauVAo02OD3%2BK0je9G%2FMn%2BNkQSv9xxzTs5OevGM1x4lqxreRFFVlGuxEcOR9EZh7WM6SNOcBgsEv7c%3D"
xz1_url = "http://newapi.kukupao.top/downloadsuccess?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=white&cryptdata=jj1ZoL5%2FqoGejDaPZQ8%2BHAHcNP8A4Dd%2B87RQnNaN%2BI3zRi%2F3IaEIkvPUjJtWukPa2PNzBCwe66HYJXPHEEU3eih%2FgsGh22uFhw1oVtt6fmVrPYDZkQzpaUSj5UsSzAgiWb7ym85J6clhD%2FE1DB5c4hP2XDSCGXkRgsqz%2FOOMhY2oqOqZl2zbQRzv0Ug1hT3IMVXJvF9vjROyt1ZMUCSXitzl3wMaE16UgRyN1t3OafbbaYrf5ZdFgAxMe3HXhNgjM%2FSZD7fBb6niep6Azpigl8w3u%2B0aSelKcTU90sv1EKzL7M7aUWQbTkXgZXv0p%2F0TCRKYD1faoBOP84ZdSwJucQ%3D%3D"
xz2_url = "http://newapi.kukupao.top/downloadsuccess?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=night&cryptdata=DGzmqzXLmkADaYGiU2o1%2BIPHGhTB45i1HXtBGI1G8YGDy00sGe3J5pI9yBIqZ%2FUtrML5VjeBScnEYt%2Bv4kRVGa4aLK8Tt1NXlhtYfwW1vqwPa6dLoSchVfUOJA5CtLDtFHpil0fRmJZWWfxeHIxsf0iyLpRgyv5FL6jGmvw52UsXQRU9X84q%2BN8WHoUUtYhSvwS6v40FhLqELesX7KfA6uG1tCK4Zsx6%2BLLhczENvnW5DCeMEbmwTyd0XmEfy%2Bg3pkpuYuGxKEs8%2Fg485jW86V%2B9bJEpQKuAC2ErrLTnw1HRs38R4i1VBPdwvPhpaMqdAHYBl32hT8lXwiRitwS98w%3D%3D"
xz3_url = "http://newapi.kukupao.top/downloadsuccess?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=white&cryptdata=uJYKyaPMI%2Fjbf0ItuzFAPXNeV%2FBLVQlGiaFJapj4I8bh5s5t82BcX6oGDgn7L6%2Bi4Pp59qbOGps033ah11lCDJ8XpsLq41EtaQWyOXUab7SWnflPe48NULKiYxeYlMaUyvg0lFO4t0yji0n8NITEPDWT9l1%2BQ%2BClMvqvncxsqW5otUotLAvbi1Abf63POgreM98D8Gl9g1tl%2F%2BjEhErAepV2vY8cwXPA971h%2BQAU2iKWLS%2B98Yw97g2SYoHg4hFWMOCvTw6Qf6IImqyRodCxmTq7jJpueF2HWT9WeCSe8ELfH67mJSCP8CaO7n86EDHYWZBcHPrtSvnKOa5z0pp24w%3D%3D"

cx_url = "http://newapi.kukupao.top/member/getgoldenbeanlog?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=night&cryptdata=KDlKhqmTW6%2BOGv1CX%2Bv9GxwNI84CTiRj1Rza%2BDYmGt8FHgg9KN1OlI2sCpnBebmj4MVDD%2F%2BIcO4KuV%2BJLCptnLR%2B6gaOYnM3bZtd4ybE0jNiKd611GqV0%2Bugt6AYkU0MYyenv7tTzlAakKpFFaKn2sZ2ZX5tkb2H8irZA8lQEfo%3D"
mhq_url = "https://m.kukupao.com.cn/member/blindbox"
qds_url = "http://newapi.kukupao.top/member/newuserachievement"
jp_url = "https://m.kukupao.com.cn/member/blindboxlog"

print("💵开始签到:")
for i, cookie in enumerate(cookies, 1):
    print("[账号]" + str(i) + ":")
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; Mi 10 Build/SKQ1.211006.001)",
        "Host": "newapi.kukupao.top",
        "Connection": "Keep-Alive",
        "Cookie": cookie
    }
    response = requests.get(url=cx_url, headers=headers)
    response_data = response.json()
    goldenbeannum = response_data["goldenbeannum"]
    response = requests.post(qds_url, headers=headers)
    response = requests.post(url=signin_url, headers=headers)
    response_data = response.json()
    keepsigncnt = response_data["keepsigncnt"]

    if response.ok:
        data = response.json()
        msg = data.get("msg")

        if msg == "\u4eca\u65e5\u5df2\u7b7e\u5230":
            print("今日已签到","豆币余额:",goldenbeannum,"\n连续签到",keepsigncnt,"天")
        elif msg == "":
            print("签到成功","豆币余额:",goldenbeannum,"\n连续签到",keepsigncnt,"天")
        elif msg == "\u7528\u6237\u9a8c\u8bc1\u5931\u8d25\uff0c\u8bf7\u91cd\u65b0\u767b\u9646":
            print("꯭❌꯭c꯭o꯭o꯭k꯭i꯭e꯭已꯭过꯭期꯭")
    else:
        print("请求失败")

print("\n💴开始分享:")
for i, cookie in enumerate(cookies, 1):
    print("[账号]" + str(i) + ":")
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }

    for j in range(6):
        response = requests.get(url=share_url, headers=headers)
        response_data = response.json()
        gblid = response_data.get("gblid")
        if "gblid" in response_data:
            print(f"分享{j+1}:\n", "✅成功 gblid:",gblid)
        else:
            print(f"分享{j+1}\n","✅分享已完成")

print("\n💶开始下载app:")

cookies = os.environ.get("kkpck").split("\n")
headers = {
    "Accept-Encoding": "gzip,deflate",
    "Cookie": ""
}

# 遍历账号列表
for i, cookie in enumerate(cookies):
    print(f'[账号]{i+1}下载')
    headers["Cookie"] = cookie
    
    response = requests.get(url=xz1_url, headers=headers)
    response_data = response.json()
    gblid = response_data.get("gblid")
    if "gblid" in response_data:
        print("✅下载app完成①:\n","成功 gblid:",gblid)
    else:
        print("✅下载已完成")

    response = requests.get(url=xz2_url, headers=headers)
    response_data = response.json()
    gblid = response_data.get("gblid")
    if "gblid" in response_data:
        print("✅下载app完成②:\n","成功 gblid:",gblid)
    else:
        print("✅下载已完成")

    response = requests.get(url=xz3_url, headers=headers)
    response_data = response.json()
    gblid = response_data.get("gblid")
    if "gblid" in response_data:
        print("✅下载app完成③:\n","成功 gblid:",gblid)
    else:
        print("✅下载已完成")

print("\n💷开始抽奖:")
for i, cookie in enumerate(cookies, 1):
    print("[账号]" + str(i) + ":")
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }
    response = requests.get(lottery_url, headers=headers)
    response_json = json.loads(response.text)
    if 'data' in response_json and 'remark' in response_json['data']:
        remark = response_json['data']['remark']
        print("抽奖结果:", remark)
    else:
        print("盲盒券已经用完了")

print("\n📢获奖记录:")
for i, cookie in enumerate(cookies, 1):
    print("[账号]" + str(i) + ":")
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }
    response = requests.get(jp_url, headers=headers)
    html_code = response.text
    soup = BeautifulSoup(html_code, 'html.parser')
    divs_with_class = soup.find_all('div', class_='name wc')
    found_names = []

    for div_with_class in divs_with_class:
        name = div_with_class.get_text(strip=True)
        if name == '1Q币':
            found_names.append(name)

    if found_names:
        for found_name in found_names:
            print("抽中过:",found_name)
    else:
        print("没有抽中过")

print("\n🎉余额更新:")
for i, cookie in enumerate(cookies, 1):
    print("[账号]" + str(i) + ":")
    headers = {
        "Accept-Encoding": "gzip,deflate",
        "Cookie": cookie
    }
    response = requests.get(url=cx_url, headers=headers)
    response_data = response.json()
    goldenbeannum = response_data["goldenbeannum"]
    print("🪙当前豆币:",goldenbeannum)
    response = requests.get(mhq_url, headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    # 查找<p>标签中的内容
    p_tags = soup.find_all('p')
    # 遍历<p>标签，找到包含盲盒券数量的那个<p>标签
    for p_tag in p_tags:
        if '全部盲盒券' in p_tag.text:
            span_tag = p_tag.find('span', id='coupon-available')
            if span_tag:
                coupon_count = span_tag.text
                print('💳全部盲盒券：', coupon_count, '张')
                break