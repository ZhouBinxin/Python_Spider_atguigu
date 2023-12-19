"""
Author：binxin
Date：2023/11/30 11:31
"""

# urllib
# 一个类型和六个方法
# get请求
# post请求 百度翻译
# ajax的get请求
# ajax的post请求
# cookie登录
# 代理

# requests
# 一个类型和六个属性
# get请求
# post请求
# 代理
# cookie 验证码

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

data = {
    'wd': '北京'
}

response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)
