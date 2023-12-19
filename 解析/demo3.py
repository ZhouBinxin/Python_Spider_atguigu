"""
下载图片

Author：binxin
Date：2023/11/26 20:06
"""
import urllib.request
from lxml import etree


# https://sc.chinaz.com/tupian/renwutupian.html
# https://sc.chinaz.com/tupian/renwutupian_2.html

def create_request(page):
    base_url = "https://sc.chinaz.com/tupian/renwutupian"
    if page == 1:
        url = base_url + '.html'
    else:
        url = f'{base_url}_{page}.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def down_load(content):
    tree = etree.HTML(content)
    src_list = tree.xpath("//img[@class='lazy']/@data-original")
    name_list = tree.xpath("//img[@class='lazy']/@alt")
    for src, name in zip(src_list, name_list):
        urllib.request.urlretrieve(f'https:{src}', f'./demo3/{name}.jpg')


if __name__ == '__main__':
    start_page = int(input("起始页码："))
    end_page = int(input("结束页码："))

    for page in range(start_page, end_page + 1):
        request = create_request(page)

        content = get_content(request)

        down_load(content)
