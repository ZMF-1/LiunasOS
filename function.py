# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 17:06:44
# @Author  : ZMF
# @FileName: function.py
# @Software: PyCharm
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
import zipfile
import os
import sys
import hashlib
import time

def unzip(path):
    with zipfile.ZipFile(path) as zf:
        zf.extractall()

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def require(ModelList):
    NoModel = []
    for Model in ModelList:
        try:
            exec("import " + Model)
        except:
            NoModel.append(Model)
    return NoModel

def usePipInstallWithList(modelList):
    for i in range(len(modelList)):
        os.system("pip install " + modelList[i])

def pause(do='继续', yon=False):
    if yon == True:
        yn = input("是否" + do + "?(y/n)")
    else:
        yn = input("是否" + do + "?")
    if yn == 'y':
        return True
    else:
        return False

def md5(text):
    '''
    :param text: the text you want to MD5
    :return: MD5 text
    '''
    md = hashlib.md5()
    md.update(text.encode("utf-8"))
    return md.hexdigest()

def write_log(input_string, output_string):
    with open(r'.\\$Sysdisk\\system.log', 'a') as f:
        time_now = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{time_now}|input:{input_string}|output:{output_string}\n')
        f.close()

def clean_log():
    with open(r'.\\$Sysdisk\\system.log', 'a', encoding='utf-8') as f:
        f.truncate(0)
        f.close()