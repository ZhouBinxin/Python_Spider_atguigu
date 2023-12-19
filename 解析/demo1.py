"""
xpath

Author：binxin
Date：2023/11/26 11:12
"""
from lxml import etree

# 本地文件
tree = etree.parse('demo1.html')
# 查找ul下的li
# li_list = tree.xpath('//body/ul/li')

# 查找有id属性的li标签
# text()获取标签内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的li标签
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找id为l1的li标签的class的属性值
# li=tree.xpath('//ul/li[@id="l1"]/@class')

# id中包含l的li标签
# li_list=tree.xpath('//ul/li[contains(@id,"l")]/text()')

# id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# id为l1和class为c1的li标签
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')

print(li_list)
# 判断列表长度
print(len(li_list))

# 服务器响应文件 response.read().decode('utf-8')
