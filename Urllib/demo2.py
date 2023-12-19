"""
一个类型和三个方法

Author：binxin
Date：2023/11/19 18:41
"""
import urllib.request

url = "https://ssr1.scrape.center/"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# response类型为HTTPResponse
print(type(response))

# 一个字节一个字节读取
# content=response.read()
# print(content)

# 返回5个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 按行读取所有内容
# content=response.readlines()
# print(content)

# 返回状态码
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取状态信息
print(response.getheaders())