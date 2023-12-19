"""
Chrome handless

Author：binxin
Date：2023/11/30 11:06
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(options=chrome_options)

    return browser


# 封装调用
browser = share_browser()
url = 'http://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu.png')
