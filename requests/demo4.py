"""
代理

Author：binxin
Date：2023/12/2 16:24
"""
import requests

url = "https://ipinfo.io/what-is-my-ip"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

proxy = {
    'http': '122.155.165.191:3128'
}

response = requests.get(url=url, headers=headers,proxies=proxy)

content = response.text

with open('demo4.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
