"""
jsonpath

Author：binxin
Date：2023/11/27 15:07
"""
import json
import jsonpath

obj = json.load(open('demo4.json', 'r', encoding='utf-8'))

# 书店所有的书
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj, '$..author')
# print(author_list)

# store下的所有元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# store下所有的price
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# 第三个书
# book_3 = jsonpath.jsonpath(obj, '$.store.book[2')
# print(book_3)

# 最后一本书
# book_end = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book_end)

# 前面的两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)

# 过滤出所有的包含isbn的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list)

# 过滤出价格低于10的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
# print(book_list)

# 所有元素
e_list = jsonpath.jsonpath(obj, '$..*')
print(e_list)
