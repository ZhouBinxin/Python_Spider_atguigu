"""
URLError/HTTPError
Author：binxin
Date：2023/11/23 20:40
"""
import urllib.request
import urllib.error

# url = "https://blog.csdn.net/qq_43546721/article/details/1340030121"
url = 'https://www.goudan111.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')
except urllib.error.URLError:
    print('系统升级')
