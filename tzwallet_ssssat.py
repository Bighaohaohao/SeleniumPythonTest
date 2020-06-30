"""
@author Maxhaohaohao
@desc 本模块是一个学习文件，使用.find_element_by_xpath 定位元素
@date 2020/06/30
说明：
"""
#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://tzwallet.ssssat.com/?id=df54e695149945e688947dc49f8777ec')
time.sleep(1)
driver.maximize_window()          # 设置浏览器全屏
time.sleep(3)
Password_login = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='login']/div[@class='main']/div[@class='web-title flex']/span[3]").click() # 定位 密码登录 按钮
phone_number = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/input").send_keys('13066859740')  # 输入手机号码
time.sleep(1)
password = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[4]/div/div[2]/input").send_keys('123456') # 输入登录密码
time.sleep(1)
# driver.find_element_by_xpath("//*[@id='app']/div/button/div/div").click() # 点击登录按钮

try:
    driver.find_element_by_class_name("md-button-content").click()
except BaseException:
    print("--------------------定位失败------------------------")
finally:
    time.sleep(10)
    driver.close()