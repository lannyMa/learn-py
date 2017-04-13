#!/usr/bin/env python
# coding=utf-8
'''

想想程序运行效果?
请输入文件名  判断文件是否存在 请输入数据

想想代码怎么实现
'''

import os


def new_file():

    #负责文件名
    while True:
        #我可以处理直到用户输入的文件正确
        #防止文件名为空 为空格
        f_name=raw_input("Enter filename > ")
        f_name="".join(f_name)
        if len(f_name)!=0 and not os.path.exists(f_name):
            break
        else:
            print "the file is exists,try again."

    content_list=[]

    #负责内容
    while True:
        content=raw_input("input somethings(q for quit)> ")
        # if content in "qQ" or not content:
        if not content:
            break
        content_list.append("%s\n"%content)

    #负责写文件
    f=file(f_name,'w')
    f.write("".join(content_list))
    f.close()

if __name__ == '__main__':
    new_file()