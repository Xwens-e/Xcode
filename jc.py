#23/7/22
#@xxxc137
import os
import requests

url = "https://ikuuu.art/user/checkin"
headers = {
    "Connection": 'keep-alive',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cache-Control": 'no-cache, must-revalidate, max-age=0',
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
    "accept": "*/*",
    "connection": "Keep-Alive",
    "Accept-Encoding": "gzip,deflate",
}
cookies_str = os.getenv("jcck")
if not cookies_str:
    print("请添加cookie")
    exit()

cookies_list = cookies_str.split("\n")

result_list = []  # 存储签到结果的列表

print("///////////////////签到开始//////////////////")

for index, cookies in enumerate(cookies_list):
    headers["Cookie"] = cookies

    response = requests.post(url=url, headers=headers)
    data = response.json()
    ret = data.get('ret')

    if ret == 1:
        msg = data.get('msg')
        # 提取 msg 中的数字
        flow = ''.join(filter(str.isdigit, msg))
        result = f"账号{index + 1} 签到成功，获得{flow}M流量"
        print("🎉",result)
        result_list.append(result)
    elif ret == 0:
        print("🍻账号{} 今日已签到".format(index + 1))
