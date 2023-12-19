"""
post请求

Author：binxin
Date：2023/11/21 16:26
"""
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求的参数 必须要编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 字符串 --> json
import json

obj = json.loads(content)
print(obj)
