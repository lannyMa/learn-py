#!/usr/bin/env python
# coding=utf-8

import os
import threading

def ping(ip)::
    result=os.system("ping -c2 %s > /dev/null 2>&1"%ip)
    if result:
        print '%s is up'%ip
    else:
        print '%s is down'%ip

if __name__ == '__main__':
    for i in range(10):
        ip="192.168.14.%s"%i
        t=threading.Thread(target=ping,args=[ip])
        t.start()
        # print ping(ip)