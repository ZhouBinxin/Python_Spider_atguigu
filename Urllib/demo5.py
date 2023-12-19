"""
get请求的quote方法

Author：binxin
Date：2023/11/21 11:10
"""
import urllib.request
import urllib.parse

# 获取 https://www.bing.com/search?q=周杰伦 网页源码
url = 'https://www.bing.com/search?q='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# 将 周杰伦 变为unicode编码格式
# 依赖于 urllib.prase
name = urllib.parse.quote('周杰伦')

url = url + name

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')
print(content)
