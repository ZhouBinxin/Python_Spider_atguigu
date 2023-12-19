"""
代理服务器

Author：binxin
Date：2023/11/24 14:25
"""
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)

# 可在快代理使用免费ip
proxies = {
    'http': '121.226.89.230:20516'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
