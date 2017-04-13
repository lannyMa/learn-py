#!/usr/bin/env python
# coding=utf-8
'''

想想程序运行效果?
请输入文件名  判断文件是否存在 请输入数据

想想代码怎么实现
'''

import os

f_name=raw_input("Enter filename > ")

if not os.path.exists(f_name):
    f=file(f_name,'w')
    content_list=[]
    while True:
        content=raw_input("input somethings(q for quit)> ")
        if content in "qQ":
            break
        content_list.append("%s\n"%content)

    if content_list:
        f.write("".join(content_list))
    f.close()
else:
    print "the file is exists"