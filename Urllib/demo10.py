"""
豆瓣电影前十页

Author：binxin
Date：2023/11/23 19:30
"""
import urllib.parse
import urllib.request


# 下载豆瓣电影前十页

def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open(f'douban{page}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("起始页码："))
    end_page = int(input("结束页码："))
    for page in range(start_page, end_page + 1):
        #         每一页都有自己的请求
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)
