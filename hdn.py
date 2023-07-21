
import hashlib
import json
import os
import re
import requests

def login(username, password, url):
    login_url = 'https://www.honpc.com/wp-login.php'
    watch_url = 'https://api.honpc.com/yrcpt/cloud/getAdvertistingDailytasks.json?token=53af4c739e366a3568b994f4eb2952fcadf7378cba078789020b24e79507c810&advertistingType=1&dailytaskid=296&dailytaskType=1&type=3&model=android&random=9c97e052-1ba9-4ff3-85da-85bb1751bae3&position=freeStrategy&platformResult=Bundle%5B%7Breward_extra_key_error_code%3D10112%2C+reward_extra_key_has_video_complete_reward%3Dfalse%2C+reward_extra_key_reward_name%3D%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8%2C+reward_extra_key_reward_propose%3D1.0%2C+reward_extra_key_error_msg%3Dserver+refuse%2C+reward_extra_key_reward_amount%3D1%7D%5D&tirmalBackOrder=2367&vcodecHImmediately=56&mac=6128D180411A3AF360D0C5FD68F3C07D0'
    
    headers = {
        "Host": "api.honpc.com",
        "token": "53af4c739e366a3568b994f4eb2952fcadf7378cba078789020b24e79507c810",
        "version": "4.4.5",
        "deviceid": "04fb9d40-6122-319b-8bea-b78d6fd322c8",
        "content-type": "text/plain;charset=utf-8",
        "content-length": "6355",
        "accept-encoding": "gzip",
        "user-agent": "okhttp-okgo/jeasonlzy",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache, must-revalidate, max-age=0",
        "Accept": "*/*",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip,deflate,br",
        "Host": "api.honpc.com",
        "Referer": "https://hw.honpc.com/"
    }
    
    # 登录
    data = {
        'log': username,
        'pwd': hashlib.md5(password.encode('utf-8')).hexdigest(),
        'mobile': ''
    }
    
    response = requests.post(login_url, headers=headers, data=data)
    print('登录结果:', response.text)
    
    # 观看广告
    response = requests.get(watch_url, headers=headers)
    print('观看广告结果:', response.text)

# 获取环境变量中的所有账号、密码和观看广告的URL
accounts_str = os.getenv('hdnck')
watch_url = os.getenv('watch_url')

# 将账号和密码分割成列表
accounts_list = re.split('[#\\n;]', accounts_str)

# 遍历账号和密码列表，依次登录并观看广告
for account in accounts_list:
    username, password = re.split('[;]', account)
    login(username, password, watch_url)
