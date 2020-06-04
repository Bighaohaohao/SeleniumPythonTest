"""
@author Maxhaohaohao
@desc 本模块是一个学习文件
@date 2020/06/03
说明：
"""

# coding=utf-8
def people(age):
    #函数体
    if age>0:
        print("正常人")
        print(get_name())
    else:
        print("不正常")

def get_name():
    return("张三三")
people(1)