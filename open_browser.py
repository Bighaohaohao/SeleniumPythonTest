"""
@author Maxhaohaohao
@desc 本模块是一个学习文件，使用python+selenium 打开浏览器等
@date 2020/06/03
说明：
"""

#coding = utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support import expected_conditions as EC


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
        if self.driver !=None:
            self.driver.maximize_window()
            if 'http://' in url:
                self.driver.get(url)
                time.sleep(10)
            else:
                print("你的URL未包含http")
        else:
            print("case执行失败")
        # self.driver.quit()

    # 封装一个方法执行浏览器的最大化、最小化、刷新、前进、后退操作
    def handle_windows(self,*args):
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
        # self.driver.quit()
    def assert_title(self,title_name=None):
    #     '''
    #     判断title是否正确
    #     '''
        if title_name !=None:
            get_title = EC.title_contains(title_name) 
            return get_title(self.driver)
    def open_url_is_true(self,url,title_name=None):
    #     '''
    #     通过title判断页面是否正确

    #     '''
        self.get_url(url)
        return self.assert_title(title_name)
    def close_driver(self):
        self.driver.close()
selfnium_driver =SelenumDriver('chrome')
selfnium_driver.handle_windows('max')
selfnium_driver.open_url_is_true(' http://www.imooc.com/article')
# selfnium_driver.open_url_is_true('http://tzwallet.ssssat.com/#/login')
selfnium_driver.close_driver()
