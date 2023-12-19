"""
selenium交互

Author：binxin
Date：2023/11/29 16:47
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://www.baidu.com'

browser.get(url)

import time

time.sleep(2)

# 获取文本框对象
input = browser.find_element(By.ID, 'kw')

# 在文本框中输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下按钮
button = browser.find_element(By.ID, 'su')

# 点击按钮
button.click()

time.sleep(2)

# 滑动窗口到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页按钮
next = browser.find_element(By.XPATH, '//a[@class="n"]')
# 点击下一页
next.click()

time.sleep(2)

# 返回上一页
browser.back()
time.sleep(2)

# 重新回到上一页
browser.forward()

time.sleep(3)

# 退出
browser.quit()
