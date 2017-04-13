#!/usr/bin/env python
# coding=utf-8


def cheng1():
    for i in range(1,10):
        for j in range(1,i+1):
            print "%s * %s = %s"%(j,i,i*j),
        # i+=1
        print

def cheng2():
    for i in range(1,10):
        for j in range(i,10):
            print "%s * %s = %s"%(j,i,i*j),
        # i+=1
        print

if __name__ == '__main__':
    cheng2()
    print "----"*20
    cheng1()