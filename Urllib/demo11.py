"""
ajax post

Author：binxin
Date：2023/11/23 20:15
"""

import urllib.request
import urllib.parse


def create_request(page):
    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=base_url, data=data, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def down_load(page, content):
    with open(f'kfc{page}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("起始页码："))
    end_page = int(input("结束页码："))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)

        down_load(page, content)
