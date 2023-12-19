"""
get请求urlencode方法

Author：binxin
Date：2023/11/21 11:26
"""
import urllib.parse
import urllib.request

# 应用场景:多个参数
# https://www.baidu.com/s?wd=周杰伦&sex=男

# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
#
# print(a)

# 获取网页源码
url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

data = urllib.parse.urlencode(data)

url = url + data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
