"""
requests 基本使用

Author：binxin
Date：2023/11/30 11:23
"""
import requests

url = 'https://www.baidu.com/'
response = requests.get(url)

# 一个类型和六个属性
# Response类型
# print(type(response))

# 设置响应的格式
# response.encoding = 'utf-8'

# 以字符串的形式返回网页源码
# print(response.text)

# 返回url地址
# print(response.url)

# 以二进制的形式返回网页源码
# print(response.content)

# 返回响应的状态码
# print(response.status_code)

# 返回响应头
print(response.headers)
