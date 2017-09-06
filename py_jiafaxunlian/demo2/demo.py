#!/usr/bin/env python
# coding=utf-8

'''
持续输入:
    直接回车,不算
    ctrl+c无法退出
    输入的是非数字

    已上这三种异常均需要扑捉并提示try again

    一共有3次猜测机会
'''

num = 0
while True:
    try:
        if(int(input("a num > "))) == 100:
            print("correct")
            break
        if num == 3:
            print("th coreect num is 100")
        else:
            print("try again")
            num += 1
    except(KeyboardInterrupt,IOError,ValueError):
        print("pls input a num")