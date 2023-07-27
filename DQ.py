import requests
import os

url = "https://wechat.dairyqueen.com.cn/memSignIn/signIn"

cookies = os.environ.get("DQck").split("\n")
for cookie in cookies:
    headers = {
        "Host": "wechat.dairyqueen.com.cn",
        "content-length": "2",
        "accept": "application/json, text/plain, */*",
        "channel": "311",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5175 MMWEBSDK/20221011 MMWEBID/3263 MicroMessenger/8.0.30.2260(0x28001E3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx22e5ce7c766b4b78",
        "tenant": "1",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://wechat.dairyqueen.com.cn",
        "x-requested-with": "com.tencent.mm",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://wechat.dairyqueen.com.cn/webview/dq/index.html?bindingAccount=15773799225&tenantId=1&channelId=311&timestamp=1690429580914&sign=a8ecadc82e6fddc6e55006e7f3d78d7e",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }

    response = requests.post(url=url, headers=headers)
    print(response.text)