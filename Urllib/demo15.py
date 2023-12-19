"""
Handler处理器

Author：binxin
Date：2023/11/24 14:16
"""
import urllib.request

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# 获取handler对象
handler = urllib.request.HTTPSHandler()

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
