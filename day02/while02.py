#!/usr/bin/env python
# coding=utf-8

'''
yn=raw_input('continue?(y/n)')

while yn not in "nN":
    print "working......"
    yn=raw_input("continue?(y/n)")
'''

while True:
    yn=raw_input('continue?(y/n)')
    if yn in "yY":
        break
    else:
        print "working..."