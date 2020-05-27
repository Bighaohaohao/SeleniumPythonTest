#coding = utf-8
from selenium import webdriver
import json
import time

#打开浏览器二次开发
class SelenumDriver:
    def __init__(self,browser):
        self.driver = self.open_browser(browser)

    def open_browser(self,browser):
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
            
    def get_url(self,url):
        # driver = open_browser('chrome')
        if self.driver !=None:
            self.driver.maximize_window()
            if 'http://' in url:
                self.driver.get(url)
                time.sleep(10)
            else:
                print("你的URL未包含http")
        else:
            print("case执行失败")
        self.driver.quit()

    # 封装一个方法执行浏览器的最大化、最小化、刷新、前进、后退操作
    def handle_windows(self,*args):
        # driver = open_browser('chrome')
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.maximize_mindow()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
               self. driver.forward()
            else:
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print("你传递的参数有问题")
        time.sleep(5)
        self.driver.quit()

selfnium_driver =SelenumDriver('chrome')
selfnium_driver.handle_windows('max')
# selfnium_driver.get_url ('http://translate.google.cn/')
selfnium_driver.get_url ('http://tzwallet.ssssat.com/#/login')
# handle_windows('200','300')
