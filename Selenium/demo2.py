"""
selenium 元素定位
Author：binxin
Date：2023/11/29 15:05
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://www.baidu.com'

browser.get(url)

# 元素定位

# 根据ID找到对象
# button = browser.find_element(By.ID,'su')

# 根据标签属性的属性值获取对象
# button = browser.find_element(By.NAME, 'wd')

# 根据xpath语句获取对象
# button = browser.find_element(By.XPATH, '//input[@id="su"]')

# 根据标签名获取对象
# button = browser.find_element(By.TAG_NAME, 'input')

# 使用bs4的语法获取对象
# button = browser.find_element(By.CSS_SELECTOR, '#su')

button = browser.find_element(By.LINK_TEXT, '新闻')
print(button)
