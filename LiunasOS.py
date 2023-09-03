# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 17:06:36
# @Author  : ZMF
# @FileName: LiunasOS.py
# @Software: PyCharm
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
import function as func
import LoginUI

need_install = func.require(["zipfile", "os", "sys", "tqdm", "time", "hashlib", "shutil", "datetime", "requests"])
if need_install != []:
    print("已检测到有缺失的库文件, ", end='')
    if func.pause(do='安装', yon=True) == True:
        func.usePipInstallWithList(need_install)
        func.write_log("system.installPackage.OK", "install|0")
        func.restart()
    else:
        func.write_log("system.installPackage.userCanceled", "install|restart")
        print("正在关机...")
        import time
        time.sleep(1)
        import os
        os.system("color 8")
        os.system("pause")
        exit()
import time
import os
from tqdm import tqdm
import shutil
import datetime
import calendar
import requests
os.system('cls')
os.system('color 0A')
time.sleep(2)
print(r"-----")
print(r"    /")
print(r"   / ")
print(r"  /  ")
print(r" /   ")
print(r"-----")
print("Loading files...")
with open(".\\$Sysdisk\\applist.liunas", "a", encoding='utf-8') as f:
    f.close()
for i in tqdm(range(64)):
    time.sleep(0.15625)
func.write_log("system.loadfile", "loded|0")
os.system('cls')
welcome = '''Disk formatted with WinImage 4.00 (c) 1993-97 Gilles Vollant
Bootsector from C.H Hochstatter

No Systemdisk. Booting from harddisk.
Starting liunasOS-DOS...

Welcome to LiunasDos 1.0
Copyright NasidaAI & ZMF Corp. All rights reserved.

Killer v1.0 Copyright 1995 Vincent Penquerc'h. All rights reserved.
Killer installed in memory.
DOSKEY installed.
DOSLFN 0.32o: loaded consuming 11840 bytes.
SHARE v7.10 (Revision 4.11.1492)
Copyright (c) 1989-2003 Datalight, Inc.

installed.

CuteMouse v1.9.1 [DOS]
Installed at PS/2 port

Now you are in LiunasDos 1.0 prompt. Type 'help' for help.


'''
if os.path.exists(".\\$Sysdisk\\sysConfig.liunas") == False:
    with open(".\\$Sysdisk\\sysConfig.liunas", "a", encoding='utf-8') as f:
        f.close()
    idu = input("输入您的账号: ")
    LoginUI.logon(idu)
    func.write_log("system.LoginUI.logon", "logon|0")
    print("即将重启")
    for i in tqdm(range(5)):
        time.sleep(1)
    func.restart()
else:
    id = input("输入您的账号: ")
    pw = input("输入您的密码: ")
    LoginUI.register(id, pw)
    func.write_log("system.LoginUI.register", "register|0")
    os.system("cls")
print(welcome)
print("Welcome, " + id)
while True:
    content = input('[' + id + ']' + "$Sysdisk>")
    with open(".\\$Sysdisk\\applist.liunas", "r", encoding='utf-8') as f:
        modelfiles = f.readlines()
        for i in range(len(modelfiles)):
            modelfiles[i] = modelfiles[i].replace('\n', '')
        f.close()
    if content in modelfiles:
        os.system("python.exe {}.py".format(content))
        func.write_log(content, "Running model {}".format(content))
    elif (content == 'help' and content.index('h') == 0) or content == '?':
        print('LiunasOS使用手册')
        print('cfo <path>          在指定的路径创建文件夹')
        print('例如: cfo $Sysdisk>abc>def')
        print('cfi <path>          在指定的路径创建文件')
        print('例如: cfi $Sysdisk>abc.txt')
        print('dfo <path>          在指定的路径删除文件夹')
        print('例如: cfo $Sysdisk>abc>def')
        print('dfi <path>          在指定的路径删除文件')
        print('例如: cfi $Sysdisk>abc.txt')
        print('shutdown          关机')
        print('reboot          重启')
        print('color <color>          切换颜色')
        print('例如: color 0b')
        print('注: color颜色帮助用指令 cohelp')
        print('dir <path>          查看指定路径下的文件')
        print('例如: dir $Sysdisk>')
        print("注: 路径末尾要加 >")
        print("echo <text>          输出文字")
        print("例如: echo Hello, LiunasOS!")
        print("cleanLog          清空日志文件")
        print("time          显示当前时间")
        print("calendar          列出日历")
        print("addUser          添加用户")
        print("nas-get <name>          下载拓展包")
        print("<name>          运行拓展包")
        func.write_log(content, "LiunasOS使用手册...")
    elif 'cfo' in content and content.index('c') == 0:
        p1 = content.replace('cfo ', '')
        if '$Sysdisk>' in p1:
            p2 = p1.replace('>', r"\\")
            p3 = ''.join(['.\\', p2])
            isExists = os.path.exists(p3)
            if not isExists:
                os.makedirs(p3)
                print('Complete!')
                func.write_log(content, 'Complete!')
            else:
                print('Error02: the folder is there.')
                func.write_log(content, 'Error02: the folder is there.')
        else:
            print('Error01: please write a real path.')
            func.write_log(content, 'Error01: please write a real path.')
    elif 'cfi' in content and content.index('c') == 0:
        p1 = content.replace('cfi ', '')
        if '$Sysdisk>' in p1:
            p2 = p1.replace('>', r"\\")
            p3 = ''.join(['.\\', p2])
            try:
                file = open(p3, 'w')
                file.close()
            except:
                print('Error07: the file is there.')
                func.write_log(content, 'Error07: the file is there.')
            print('Complete!')
            func.write_log(content, 'Complete!')
        else:
            print('Error01: please write a real path.')
            func.write_log(content, 'Error01: please write a real path.')
    elif 'dfo' in content and content.index('d') == 0:
        p1 = content.replace('dfo ', '')
        if '$Sysdisk>' in p1:
            p2 = p1.replace('>', r"\\")
            p3 = ''.join(['.\\', p2])
            try:
                shutil.rmtree(p3)
            except:
                print('Error01: please write a real path.')
                func.write_log(content, 'Error01: please write a real path.')
            else:
                print('Complete!')
                func.write_log(content, 'Complete!')
        else:
            print('Error01: please write a real path.')
            func.write_log(content, 'Error01: please write a real path.')
    elif 'dfi' in content and content.index('d') == 0:
        p1 = content.replace('dfi ', '')
        if '$Sysdisk>' in p1:
            p2 = p1.replace('>', r"\\")
            p3 = ''.join(['.\\', p2])
            try:
                os.remove(p3)
            except:
                print("Error01: please write a real FILE's path.")
                func.write_log(content, "Error01: please write a real FILE's path.")
            else:
                print('Complete!')
                func.write_log(content, 'Complete!')
        else:
            print('Error01: please write a real path.')
            func.write_log(content, 'Error01: please write a real path.')
    elif content == 'shutdown' and content.index('s') == 0:
        func.write_log(content, "shutdown|0")
        break
    elif content == 'reboot' and content.index('r') == 0:
        func.restart()
        func.write_log(content, "restart|0")
    elif 'color' in content and content.index('c') == 0:
        os.system(content)
        func.write_log(content, "color|0")
    elif content == 'cohelp' and content.index('c') == 0:
        print('''
    颜色属性由两个十六进制数字指定 -- 第一个
    对应于背景，第二个对应于前景。每个数字
    可以为以下任何值:

        0 = 黑色       8 = 灰色
        1 = 蓝色       9 = 淡蓝色
        2 = 绿色       A = 淡绿色
        3 = 浅绿色     B = 淡浅绿色
        4 = 红色       C = 淡红色
        5 = 紫色       D = 淡紫色
        6 = 黄色       E = 淡黄色
        7 = 白色       F = 亮白色
        ''')
        func.write_log(content, "颜色属性由两个十六进...")
    elif 'dir' in content and content.index('d') == 0:
        p1 = content.replace('dir ', '')
        if '$Sysdisk>' in p1:
            p2 = p1.replace('>', r"\\")
            p3 = ''.join(['.\\', p2])
            try:
                os.system('dir ' + p3)
                func.write_log(content, "dir|0")
            except:
                print('Error01: please write a real path.')
                func.write_log(content, "Error01: plase write a real path.")
        else:
            print('Error01: please write a real path.')
    elif 'echo' in content and content.index('e') == 0:
        answer = content.replace('ECHO ', '')
        func.write_log(content, answer)
        print(answer)
    elif 'cleanLog' in content and content.index('c') == 0:
        func.clean_log()
        func.write_log(content, "cleanLog|0")
    elif 'time' in content and content.index('t') == 0:
        now = datetime.datetime.now()
        other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print(other_StyleTime)
        func.write_log(content, other_StyleTime)
    elif 'calendar' in content and content.index('c') == 0:
        yy = int(input("Year: "))
        mm = int(input("Month: "))
        print(calendar.month(yy, mm))
        func.write_log(content, "calendar.month({}, {})".format(yy, mm))
    elif 'addUser' in content and content.index('a') == 0:
        idn = input("输入您的账号: ")
        LoginUI.logon(idn)
        func.write_log("system.LoginUI.logon", "logon|0")
        print("即将重启...")
        for i in tqdm(range(5)):
            time.sleep(1)
        func.restart()
    elif 'nas-get' in content and content.index('n') == 0:
        p1 = content.replace('nas-get ', '')
        mList = requests.post(url=r"http://liunas.atwebpages.com/liunas-model/list.txt", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"})
        with open("list.txt", "wb") as tempn1:
            tempn1.write(mList.content)
            tempn1.close()
        with open("list.txt", "r", encoding='utf-8') as tempn2:
            tempn3 = tempn2.read()
            tempn2.close()
        mList2 = []
        mList2 = tempn3.split("|")
        if p1 in mList2:
            mdnei = requests.post(url=r"http://liunas.atwebpages.com/liunas-model/{}-setup.txt".format(p1), headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"})
            with open("{}-setup.py".format(p1), "wb") as mnei:
                mnei.write(mdnei.content)
                mnei.close()
            os.system("python.exe {}-setup.py".format(p1))
            print("Install ok!")
            func.write_log(content, "Install ok!")
            os.remove("{}-setup.py".format(p1))
            func.write_log("system.tempfile.remove.modelsetupfile", "system|0")
        else:
            print("Error08: ERROR: No matching distribution found for {}".format(p1))
            func.write_log(content, "Error08: ERROR: No matching distribution found for {}".format(p1))
        os.remove("list.txt")
        func.write_log("system.tempfile.remove.modellistfile", "system|0")
    else:
        print("Error06: we can't find the command or file: " + content)
        func.write_log(content, "Error06: we can't find the command or file: " + content)
