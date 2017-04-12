#!/usr/bin/env python
# coding=utf-8

print "*"*20
print "#"*20

#无return的函数返回None
def pstar(f):
    print f*20

pstar       #函数的引用
pstar('&')
pstar('-')
pstar('^')

a=pstar
print a,a('$')