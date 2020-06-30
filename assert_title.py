"""
@author Maxhaohaohao
@desc 本模块是一个学习文件，通过title判断当前打开页面是否正确
@date 2020/06/03
说明：
"""

# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("http://tzwallet.ssssat.com/#/login")
title_name = driver.title
if '企业钱包' in title_name:
    print("打开正确")
else:
    print("打开错误")

titl_a = EC.title_is("企业钱包")
print(titl_a(driver))
title_b = EC.title_contains("企业钱包")
print(title_b(driver))
time.sleep(10)
driver.close()
