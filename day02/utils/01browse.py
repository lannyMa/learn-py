#!/usr/bin/env python
# coding=utf-8
'''使用webbrowser刷博客

使用webbrowser刷博客
'''
# import webbrowser
#
# url="http://www.cnblogs.com/iiiiher"
#
# counter=1
# while counter<=10:
#     webbrowser.open_new_tab(url)
#     counter+=1
#

'''if over 10 tabs,kill firefox.

every 0.5s open a tab 
'''
import webbrowser
import time
import os
url="http://www.cnblogs.com/iiiiher"

counter=1
while counter<=10:
    webbrowser.open_new_tab(url)
    counter+=1
    time.sleep(0.5)
    # if counter % 10 == 0:
    if not counter % 10:
        os.system("killall firefox")