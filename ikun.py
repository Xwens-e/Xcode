#23/8/31
#@xxxc137
import os
import requests
from bs4 import BeautifulSoup

login_url = "https://ikuuu.art/auth/login"
sign_url = "https://ikuuu.art/user/checkin"
user_url = "https://ikuuu.art/user"

cookie_values = os.environ.get("jcck").splitlines()
for i, cookie in enumerate(cookie_values, 1):
    values = cookie.split("#")
    print("[账号]" + str(i) + ":")
    headers = {
        "Connection": 'keep-alive',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cache-Control": 'no-cache, must-revalidate, max-age=0',
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.58 Mobile Safari/537.36",
        "accept": "*/*",
        "connection": "Keep-Alive",
        "Accept-Encoding": "gzip,deflate",
    }

    data = values[0]
    
    print("✏️状态:")
    session = requests.Session()
    response = session.post(login_url,headers=headers,data=data)
    data = response.json()
    msg = data["msg"]
    print("– ",msg)
    
    print("📝签到:")
    response = session.post(sign_url,headers=headers)
    data = response.json()
    response = session.get(user_url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    counter_element = soup.find("span", {"class": "counter"})
    counter = counter_element.text.strip()
    msg = data["msg"]
    print("– ",msg ,"流量余额:",counter,"GB\n")