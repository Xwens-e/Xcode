#23/7/24
#@xxxc137
#变量：ymgck 用账号密码登录 账号;密码 多号换行隔开
import os
import requests
from bs4 import BeautifulSoup

login_url = 'http://www.ymg.one/wp-login.php'
qiandao_url = 'http://www.ymg.one/wp-admin/admin-ajax.php?action=user_qiandao&ie=utf-8'

# 创建 session 对象
session = requests.Session()

# 获取登录页面
login_page = session.get(login_url)

# 使用 BeautifulSoup 解析页面
soup = BeautifulSoup(login_page.content, 'html.parser')

# 获取登录所需的 hidden 表单字段
login_data = {}
for input_tag in soup.find_all('input'):
    if input_tag.get('type') != 'hidden':
        continue
    login_data[input_tag.get('name')] = input_tag.get('value')

# 设置用户名和密码
cookies_str = os.getenv("ymgck")  # 获取外置变量 ck
account_passwords = cookies_str.split("\n")  # 多个账号用#分隔
for account_password in account_passwords:
    account_password_parts = account_password.split(";")  # 使用分号拆分账号和密码
    if len(account_password_parts) != 2:
        print(f'账号密码格式错误：{account_password}')
        continue
        
    account, password = account_password_parts
    login_data['log'] = account
    login_data['pwd'] = password

    # 替换为正确的登录按钮字段值
    login_data['wp-submit'] = '登录'  # 或者使用'登陆'

    print("///////////////签到开始///////////////")
    
    # 发送登录请求
    response = session.post(login_url, data=login_data)

    # 检查登录是否成功
    if response.status_code == 200:
        print(f'{account} 登录成功')  # 打印账号名称

        # 发送签到请求
        response = session.get(qiandao_url)

        # 解析签到结果
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
    else:
        print(f'{account} 登录失败')