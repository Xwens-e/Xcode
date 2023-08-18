#23/7/24
#@xxxc137
#变量：ymgck 用账号密码登录 账号;密码 多号换行隔开
import os
import requests
from bs4 import BeautifulSoup

login_url = 'http://www.ymg.one/wp-login.php'
qiandao_url = 'http://www.ymg.one/wp-admin/admin-ajax.php?action=user_qiandao&ie=utf-8'
cx_url = 'http://www.ymg.one/user'

print("///////////////开始签到///////////////")

session = requests.Session()

login_page = session.get(login_url)

soup = BeautifulSoup(login_page.content, 'html.parser')

login_data = {}
for input_tag in soup.find_all('input'):
    if input_tag.get('type') != 'hidden':
        continue
    login_data[input_tag.get('name')] = input_tag.get('value')

cookies_str = os.getenv("ymgck") 
account_passwords = cookies_str.split("\n")
for account_password in account_passwords:
    account_password_parts = account_password.split(";")
    if len(account_password_parts) != 2:
        print(f'账号密码格式错误：{account_password}')
        continue
        
    account, password = account_password_parts
    login_data['log'] = account
    login_data['pwd'] = password

    login_data['wp-submit'] = '登录'
    response = session.post(login_url, data=login_data)   
    if response.status_code == 200:
        print("[账号]",f'{account} 登录成功')
        response = session.get(qiandao_url)
        json_response = response.json()
        response = session.get(cx_url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        jinbi_element = soup.find("span", {"class": "jinbi"})
        jinbi = jinbi_element.text.strip()
        dou_element = soup.find("span", {"class": "dou"})
        dou = dou_element.text.strip()
        # 解析签到结果
        if "msg" in json_response:
            if json_response["msg"] == "\u7b7e\u5230\u6210\u529f\uff0c\u8d60\u90010.5\u94bb\u77f3":
                print("– 🎉签到成功，获得0.5个钻石","\n–",jinbi,"\n–",dou,"\n")
            elif json_response["msg"] == "\u4eca\u65e5\u5df2\u7b7e\u5230\uff0c\u8bf7\u660e\u65e5\u518d\u6765":
                print("– 📣已经签到过了","\n–",jinbi,"\n–",dou,"\n")
            elif json_response["msg"] == "\u8bf7\u767b\u5f55\u540e\u7b7e\u5230":
                print("❎账号密码错误")
        else:
            print("❎请求失败")
    else:
        print(f'{account} 登录失败')
        
