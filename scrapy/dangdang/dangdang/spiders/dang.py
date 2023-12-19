import scrapy
from dangdang.items import DangdangItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # src=//ul[@id="component_59"]/li//img/@src
        # alt=//ul[@id="component_59"]/li//img/@alt
        # price=//ul[@id="component_59"]/li//span[@class="search_now_price"]/text()
        # 所有的sector对象，都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src is None:
                src = li.xpath('.//img/@src').extract_first()
            # 第一张图片和其他的图片的标签属性不一样
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//span[@class="search_now_price"]/text()').extract_first()

            book = DangdangItem(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book
        pass
