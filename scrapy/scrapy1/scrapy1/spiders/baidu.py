import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫时 使用的值
    name = "baidu"
    # 运行访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址
    start_urls = ["https://www.baidu.com"]

    # 执行了start_urls之后执行的方法 方法中的response就是返回的那个对象
    # 相当于response=urllib.requests.uelopen()
    def parse(self, response):
        print("PinHsin")
