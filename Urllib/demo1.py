"""
使用urllib获取网页的源码

Author：binxin
Date：2023/11/19 18:16
"""
import urllib.request

url = "https://ssr1.scrape.center/"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应中的页面的源码
# read() 返回的是字节形式的二进制数
# 将二进制数据转换为字符串——解码 decode('编码的格式')
content = response.read().decode('utf-8')

# 打印数据
print(content)
