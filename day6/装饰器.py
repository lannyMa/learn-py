#!/usr/bin/env python
# coding=utf-8

def login(func):
    def innner():
        print 'login  '
        # return func
        func()

    return innner


def tv():
    print 'tv page'


tv = login(tv)
# print tv
tv()

print hello world

