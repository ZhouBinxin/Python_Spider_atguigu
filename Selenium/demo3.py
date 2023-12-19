"""
元素信息

Author：binxin
Date：2023/11/29 16:31
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element(By.ID, 'su')

# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)

a = browser.find_element(By.LINK_TEXT, '新闻')
# 获取元素文本
print(a.text)
