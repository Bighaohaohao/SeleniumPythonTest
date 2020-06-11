"""
@author Maxhaohaohao
@desc 本模块是一个学习文件，使用.find_element_by_partial_link_text 定位超链接下的元素
@date 2020/06/03
说明：
"""

#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
# 使用.find_element_by_partial_link_text 定位超链接下的元素
# driver.get('https://www.imooc.com/course/list')
# time.sleep(5)
# driver.find_element_by_partial_link_text('用技术打造小程序简历，让面试官耳目一新').click()

# 模态框及焦点定位
driver.get('https://www.imooc.com/')
driver.find_elements_by_id("js-signin-btn").click()
time.sleep(3)
driver.find_elements_by_class_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_elements_by_class_name("password")
element.send_keys('xu221168')
driver.find_elements_by_class_name("moco-btn-lg").click()
time.sleep(2)
driver.get('https://coding.imooc.com/')
time.sleep(3)


driver.close()
