#热度星客(种草任务更新)
#23/7/26 
#@xxxc137
#微信链接:#小程序://热度星客/NgVlu6iTKhs95Yp
#任务:每天签到大概0.02-0.1 有浏览、点赞、分享任务可以抽奖 默认抽奖3次(抽奖不会算了就一次) 抽奖金额0.01-88
#变量名 rd_ck 抓authori-zation 多号换行隔开
import requests
import os
import re
import time

authorization_headers = os.environ.get("rd_ck").split("\n")

ll_url = "https://m.reduxingke.com/api//friends/task/account?type=browse"  # get
sign_url = "https://m.reduxingke.com/api/usersign/sign"  # post
dz_url = "https://m.reduxingke.com/api//friends/task/account?type=thumb"  # get
share_url = "https://m.reduxingke.com/api//friends/task/account?type=share"  # get
cj_url = "https://m.reduxingke.com/api//friends/task/new_draw"  # post

for index, auth_header in enumerate(authorization_headers, start=1):
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Authorization": auth_header
    }
    
    print("账号", index)
    
    sign_response = requests.post(url=sign_url, headers=headers)
    print("📮开始签到:")
    print(sign_response.text)

    print("💌浏览任务:")
    for i in range(3):
        ll_response = requests.get(url=ll_url, headers=headers)
        if ll_response.ok:
            ll_result = ll_response.text
            print("第", i+1, "次浏览任务结果:")
            print(ll_result)
        else:
            print("第", i+1, "次浏览任务失败")
        time.sleep(2)

    dz_response = requests.get(url=dz_url, headers=headers)
    print("👍🏿点赞任务:")
    print(dz_response.text)

    share_response = requests.get(url=share_url, headers=headers)
    print("✨分享任务:")
    print(share_response.text)

    print("等待两秒")
    time.sleep(2)

    print("🎁开始抽奖")
    print("抽奖:")
    data = {"type": "thumb", "order_id": ""}
    cj_response = requests.post(url=cj_url, headers=headers, data=data)
    print(cj_response.text)