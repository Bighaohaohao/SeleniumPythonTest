"""
@author Maxhaohaohao
@desc 本模块是一个学习文件，使用.find_element_by_xpath 定位元素
@date 2020/06/30
说明：
"""
#coding = utf-8
from selenium import webdriver
import json
import time
from selenium.webdriver.support import expected_conditions as EC


class SelenumDriver:
    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def open_browser(self, browser):
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

    def get_url(self, url):
        if self.driver != None:
            self.driver.maximize_window()
            if 'http://' in url:
                self.driver.get(url)
                time.sleep(2)
            else:
                print("你的URL未包含http")
        else:
            print("case执行失败")
    
     # 封装一个方法执行浏览器的最大化、最小化、刷新、前进、后退操作
    def handle_windows(self, *args):
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
        time.sleep(2)

    def assert_title(self, title_name=None):
    #     '''
    #     判断title是否正确
    #     '''
        if title_name != None:
            get_title = EC.title_contains(title_name) 
            return get_title(self.driver)
    def open_url_is_true(self, url, title_name=None):
    #     '''
    #     通过title判断页面是否正确

    #     '''
        self.get_url(url)
        return self.assert_title(title_name)
    #     '''
    #     定位元素

    #     '''
    def Login_test(self):
        Password_login = self.driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='login']/div[@class='main']/div[@class='web-title flex']/span[3]").click() # 定位 密码登录 按钮
        phone_number = self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/input").send_keys('13066859740')  # 输入手机号码
        time.sleep(1)
        password = self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[4]/div/div[2]/input").send_keys('123456') # 输入登录密码
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name("md-button-content").click()
        except BaseException:
            print("--------------------定位失败------------------------")
        finally:
            time.sleep(10)
            self.driver.close()


    def close_driver(self):
        self.driver.close()

selfnium_driver = SelenumDriver('chrome')
selfnium_driver.handle_windows('max')
selfnium_driver.open_url_is_true('http://tzwallet.ssssat.com/?id=df54e695149945e688947dc49f8777ec')
selfnium_driver.Login_test()
time.sleep(10)
selfnium_driver.close.driver()