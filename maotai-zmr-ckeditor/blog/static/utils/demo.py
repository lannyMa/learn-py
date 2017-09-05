#!/usr/bin/env python
# coding=utf-8
import os
from jinja2 import Template
import time

now = (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

def bbs():
    with open("date.html", 'r') as f:
        data = f.read()
    tmp=Template(data)
    data=tmp.render(now=now,user_list=['aaron','bob','cristin','danny'])
    print (data)
    # return data.encode("utf-8")
    with open('date_now.html','w') as f:
        f.write(str(data.encode("utf-8")))
bbs()