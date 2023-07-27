#23/7/27
#@xxxc137
import requests
import json
import os

url = "https://youshenghuo.11185.cn/ZxptRestYshWECHAT/mbr/signin/addSignIn"

authorization_headers = os.environ.get("ysh_ck").split("\n")
responses = []  # 用于保存每个账号的响应结果

for index, auth_header in enumerate(authorization_headers, start=1):
    headers = {
        "Host": "youshenghuo.11185.cn",
        "Accept": "application/json, text/plain, */*",
        "Channel": "wechat",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5175 MMWEBSDK/20221011 MMWEBID/3263 MicroMessenger/8.0.30.2260(0x28001E3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Content-Type": "application/json",
        "Origin": "https://youshenghuo.11185.cn",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://youshenghuo.11185.cn/wx/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": auth_header
    }

    data = {
        # 根据请求参数的实际情况进行填充
    }

    try:
        json_data = json.dumps(data)  # 将请求参数转换为 JSON 格式
        headers["Content-Length"] = str(len(json_data))  # 计算实际的内容长度并更新头部字段的值
        response = requests.post(url=url, headers=headers, data=json_data)
        response.raise_for_status()
        responses.append(response.text)  # 保存响应结果到列表中
    except requests.exceptions.RequestException as e:
        responses.append(str(e))  # 保存异常信息到列表中

# 输出每个账号的响应结果
for index, response in enumerate(responses, start=1):
    print(f"账号 {index} 的响应结果:")
    print(response)
    print("--------------------")