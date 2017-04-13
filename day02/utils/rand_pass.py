#!/usr/bin/env python
# coding=utf-8
'''生成随机密码


'''

import string
import random
from sys import argv

def general_password(num=10):
    ch = string.letters + string.digits
    str = ""
    for i in range(num):
        op = random.choice(ch)
        str.join(op)

    return str

#使用join列表的方式,变量id未发生改变,效率更高
def general_password2(num=10):
    ch = string.letters + string.digits
    alist=[]
    for i in range(num):
        op = random.choice(ch)
        alist.append(op)
        result="".join(alist)
    return result

if __name__ == '__main__':
    if len(argv) != 1:
        num = int(argv[1])
        print general_password2(num)
    else:
        print "[USAGE: python general_password.py [num]]"

        print "this is the default 10 bit password: ", general_password2()