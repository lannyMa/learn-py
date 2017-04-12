#!/usr/bin/env python
# coding=utf-8

import os


def ping(ip):
    result=os.system("ping -c2 %s > /dev/null 2>&1"%ip)
    if result:
        return '%s is up'%ip
    else:
        return '%s is down'%ip

if __name__ == '__main__':
    for i in range(10):
        ip="192.168.14.%s"%i
        print ping(ip)