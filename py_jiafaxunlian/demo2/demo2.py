#!/usr/bin/env python
# coding=utf-8


'''
输入n后退出
输入nxxxx也退出
其他输入均表示继续


'''


while True:
    try:
        op = input("Again?[y]").lower()
        if op and op[0]=="n":
            break
    except(KeyboardInterrupt,EOFError):
        print("pls input a y/n")