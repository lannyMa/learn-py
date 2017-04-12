#!/usr/bin/env python
# coding=utf-8

import string
import random
from sys import argv


def general_password(num=10):
    ch = string.letters + string.digits
    str = ""
    for i in range(num):
        op = random.choice(ch)
        str += op
    return str

if __name__ == '__main__':
    if len(argv) != 1:
        num = int(argv[1])
        print general_password(num)
    else:
        print "[USAGE: python general_password.py [num]]"

        print "this is the default 10 bit password: ", general_password()