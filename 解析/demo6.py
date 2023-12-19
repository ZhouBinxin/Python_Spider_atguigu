"""
bs4基本使用

Author：binxin
Date：2023/11/27 18:23
"""
from bs4 import BeautifulSoup

# 解析本地文件
# 默认打开文件的编码格式为gbk
soup = BeautifulSoup(open('demo6.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的数据
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的函数
# find
# 返回第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值来找到对应的标签对象
# print(soup.find('a',title='a2'))

# 根据class的值来找到对应的标签对象 注意的是class需要添加下划线
# print(soup.find('a', class_="a1"))

# find_all
# 返回所有a标签，返回的是一个列表
# print(soup.find_all('a'))

# 返回所有的a和span
# print(soup.find_all(['a', 'span']))

# 查找前几个数据
# print(soup.find_all('li',limit=2))

# select
# 返回一个列表，多个数据
# print(soup.select('a'))

# 通过.代表class
# print(soup.select('.a2'))

# print(soup.select('#l1'))

# 属性选择器
# li标签中包含id标签
# print(soup.select('li[id]'))

# 查找li标签中id=l2
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# div下的li
# print(soup.select('div li'))

# 子代选择器 第一级子标签
# print(soup.select('div > ul > li'))

# 找到a标签和li标签
# print(soup.select('a,li'))

# 节点信息
# 获取节点内容
# obj = soup.select('#d1')[0]
# 如果标签对象中，除了内容还有标签，那么string获取不到内容，但是get_text()可以
# print(obj.get_text())
# print(obj.string)

# 节点属性
obj = soup.select('#p1')[0]
# name是标签名
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点属性
obj = soup.select('#p1')[0]

print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
