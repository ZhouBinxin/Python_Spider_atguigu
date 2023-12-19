"""
post请求

Author：binxin
Date：2023/12/2 16:05
"""
import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

data = {
    'kw': 'eye'
}

response = requests.post(url=url, data=data, headers=headers)

content = response.text

import json

obj = json.loads(content)
print(obj)
