"""
古诗文网

Author：binxin
Date：2023/12/2 16:39
"""
# 进入主页面

# 登录所需参数
# __VIEWSTATE: 0l7aRwy/rgg6Vqp67IkeKC4Vual1jYsWsWILZ8PaSs39ayyuVom0o0OPgJKwNdCcDdpRRjvteZxMTnq0PiAma58XmjDrM+gMnMWWhqGzfoXeoKgOBNQuf4dDaBPVyJe4aw5GRBUPbTu3C8QwThnqAWG4uZI=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: pinhsin@163.com
# pwd: zbx123456
# code: Tb4C
# denglu: 登录

import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# 获取页面源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码 获取__VIEWSTATE __VIEWSTATEGENERATOR
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn/' + code

# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 获取验证码图片，然后在控制台输入验证码
content_code = response_code.content

with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

code_name = input('请输入验证码')

# 开始登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from: http': '//so.gushiwen.cn/user/collect.aspx',
    'email': ' pinhsin@163.com',
    'pwd': ' zbx@1018',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text

with open('demo5.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
