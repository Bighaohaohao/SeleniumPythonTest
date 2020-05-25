#coding = utf-8
from selenium import webdriver
import json
import time

def open_browser(browser):
    try:
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'ie':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Edge()

        return driver
    except:
        print("打开浏览器失败")
        return None

def get_url(url):
    driver = open_browser('chrome')
    if driver !=None:
        if 'http://' in url:
            driver.get(url)
            time.sleep(10)
        else:
            print("你的URL未包含http")
    else:
        print("case执行失败")

#driver1 = open_browser ('chrome')
# get_url('www.imooc.com')
get_url('http://tzwallet.ssssat.com/#/login')
