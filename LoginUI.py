# -*- coding: utf-8 -*-
# @Time    : 2022/12/31 14:09
# @Author  : ZMF
# @FileName: LoginUI.py
# @Software: PyCharm
# @Blog    ：https://cdt-1.github.io
import function as func

def register(username,password):#登录功能，且与存储用户表的文本文件进行比较
    #验证用户名
    shuju=readfile()
    jg1 = 0
    i = 0
    while (i < len(shuju)):
        if (username == shuju[i]["用户名"]):
            print("用户名正确")
            jg1 = 1
            break
        i += 1
    # 用户名错误将不再验证密码
    if (jg1 != 1):
        print("用户名错误")
    # 验证密码
    if (jg1 == 1):
        jg2 = 0
        i = 0
        while (i < len(shuju)):
            if (func.md5(password) == shuju[i]["密码"]):
                print("密码正确")
                jg2 = 1
                break
            i += 1
        if (jg2 != 1):
            print("密码错误")
            func.write_log("LoginUI.password.error", "system.warning")

def logon(username):#注册功能，且以正确格式存入文本文件
    shuju=readfile()
    jg3 = 0
    i = 0
    while (i < len(shuju)):
        if (username == shuju[i]["用户名"]):
            print("用户名已经存在")
            jg3 = 1
            break
        i += 1
    if(jg3 == 0):
        while True:
            password = input("请输入密码(密码不能小于6位，且不能为纯数字): ")
            if (str.isdigit(password)==1) or (len(password)<6):
                    print("密码格式错误")
            else:
                break
        passwordagain=input("请再次确认密码: ")
        while True:
            if(password==passwordagain):
                break
            else:
                print("两次密码不一致")
                passwordagain = input("请再次确认密码: ")
        # 将注册的用户信息存储到文本文件中
        f = open(".\\$Sysdisk\\sysConfig.liunas", mode='a+', encoding="utf8")
        if shuju == []:
            f.write("用户名:{},密码:{}".format(username, func.md5(password)))
        if shuju != []:
            f.write("\n用户名:{},密码:{}".format(username, func.md5(password)))
        print("注册成功")
        f.close()

def readfile():#将数据转换成列表字典形式，放在data.txt中便于后面登录与注册存放数据
    f = open(".\\$Sysdisk\\sysConfig.liunas", "r+", encoding="utf8")
    shuju = []
    b = []
    aa = {}
    for line in f.readlines():
        line = line.strip('\n')
        a = line.split(' ')
        i = 0
        while i < len(a):
            b = a[i].split(',')
            i += 1

        j = 0
        while j < len(b):
            if b == " ":
                break
            c = b[j].split(':', 1)
            aa[c[0]] = c[1]
            i += 1
            j += 1

        shuju.append(aa.copy())  # copy是为了防止添加是数据类型不同出错
    f.close()
    return shuju