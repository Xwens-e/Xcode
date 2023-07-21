#23/7/19
#@xxxc137
import os
import requests

url = "http://newapi.kukupao.top/tuhao/signin?phonetype=Mi+10&phonebrand=Xiaomi&osversion=12&osversioncode=31&version=11.7.10&versioncode=129&channel=%E5%AE%98%E7%BD%91&channelid=1&appid=1&sw=1080&sh=2339&dt=%E6%89%8B%E6%9C%BA&network=2014&carrier=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&oaid=2ac4ea344ca1d124&um_oaid=2ac4ea344ca1d124&miui=1&skin=white&cryptdata=nobiE%2BtIzCBS%2FymcImybXbLUvoqF9x%2BsouvTU0eo2FZdJ9EhD%2F2YsmYdtCHg9fRu5xNzhyS5orjZYWdnsSotbW3y%2F%2BUqiAmAqmiOJfH4brSX%2BUM4bbA07EQn2MpvdbsyY1tXO8cfNAC9DG503cifkuDCgETseVyII%2FgtgNAAG3k%3D"
headers = {
    "Connection": 'keep-alive',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cache-Control": 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
    "Host": "newapi.kukupao.top",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
    "accept": "*/*",
    "connection": "Keep-Alive",
    "Accept-Encoding": "gzip,deflate"
}
# 获取青龙外置变量的值
kkpck = os.environ.get("kkpck")
cookies_list = kkpck.split("\n")

for cookie in cookies_list:
    if cookie.startswith("#"): # 以#开头的行将被忽略
        continue

    try:
        response = requests.post(url=url, headers=headers, cookies={"Cookie": cookie})

        if response.ok:
            data = response.json()
            msg = data.get("msg")

            if msg == "\u4eca\u65e5\u5df2\u7b7e\u5230":
                print("🎈已经签到过了")
            elif msg == "":
                print("🎉签到成功")
            elif msg == "\u7528\u6237\u9a8c\u8bc1\u5931\u8d25\uff0c\u8bf7\u91cd\u65b0\u767b\u9646":
                print("❌cookie已过期")
        else:
            print("请求失败")
    except Exception as e:
        print("发生异常:", str(e))