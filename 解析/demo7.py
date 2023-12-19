"""
bs4解析

Author：binxin
Date：2023/11/28 10:37
"""
import urllib.request
from bs4 import BeautifulSoup

url = 'https://ssr1.scrape.center/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

# //h2[@class='m-b-sm']/text()
name_list = soup.select('h2[class="m-b-sm"]')

for name in name_list:
    print(name.get_text())
