#!/usr/bin/env python
#coding=utf-8



def login(func):
    def inner():
        print 'login success!'
        func()
    return inner
def tv():
    print 'tv page'

tv=login(tv)
tv()
print "#"*50