#!/usr/bin/env python
# coding=utf-8

import os

for i in range(1,255):
    ip="192.168.14.%s"%i
    result=os.system("ping -c2 %s > /dev/null 2>&1"%ip)
    if not result:
        print '%s is up'%ip
    else:
        print '%s is down'%ip