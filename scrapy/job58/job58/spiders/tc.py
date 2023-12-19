import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["cc.58.com"]
    start_urls = ["https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&button=%E6%90%9C%C2%A0%E7%B4%A2"]

    def parse(self, response):
        # 字符串
        # content=response.text
        # 二进制数据
        # content = response.body
        # print(content)
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print(span.extract())
