# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 14:14
# @Author  : Scavenger
# @FileName: Python基础.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

"""
25.什么是反射？以及应用场景？


"""


def f1():
    print("f1是这个函数的名字！")


s = "f1"
# print("%s是个字符串" % s)


def login():
    print("这是一个登陆页面！")


def logout():
    print("这是一个退出页面！")


def home():
    print("这是网站主页面！")


import commons


def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if inp == "login":
        commons.login()
    elif inp == "logout":
        commons.logout()
    elif inp == "home":
        commons.home()
    else:
        print("404")


if __name__ == '__main__':
    run()