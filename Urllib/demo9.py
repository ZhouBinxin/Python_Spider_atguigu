"""
ajax get请求
Author：binxin
Date：2023/11/23 19:16
"""
import urllib.request

# 获取豆瓣电影第一页的数据，并且保存起来
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 数据下载到本地
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)

with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
