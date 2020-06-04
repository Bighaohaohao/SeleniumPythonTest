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
driver.get('https://www.imooc.com/course/list')
time.sleep(5)
driver.find_element_by_partial_link_text('用技术打造小程序简历，让面试官耳目一新').click()
driver.close()
