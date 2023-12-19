"""
代理池

Author：binxin
Date：2023/11/24 14:47
"""
import random
import urllib.request

proxies_pool = [
    {'http': '42.249.189.41:17666'},
    {'http': '27.154.221.103:19542'}
]

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
