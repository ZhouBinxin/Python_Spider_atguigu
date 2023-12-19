# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果使用管道的话,就必须在settings中开启管道
class DangdangPipeline:
    # 在爬虫文件开始前就执行
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        self.fp.write(str(item))

        # 以下模式不推荐,每传递一个对象就打开一次文件,对文件的操作过于频繁
        # with open('book.json','a',encoding='utf-8') as fp:
        #     # write方法必须写一个字符串
        #     fp.write(str(item))

        return item

    # 在爬虫文件执行后再执行
    def close_spider(self, spider):
        self.fp.close


import urllib.request


# 多条管道下载
# 定义管道类
# 在settings中开启管道
# "dangdang.pipelines.DangDangDownloadPipeline": 301
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = "http:" + item.get("src")
        filename = "./books/" + item.get("name") + ".jpg"
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
