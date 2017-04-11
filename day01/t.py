#!/usr/bin/env python
#coding=utf-8
import star

star.pstar()


def foo():
    print 'in foo'
    bar()

def bar():
    print 'in bar'
    # foo()

if __name__ == '__main__':
    foo()