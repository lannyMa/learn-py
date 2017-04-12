#!/usr/bin/env python
# coding=utf-8

#shell循环
#for i in `seq 1 10`;do echo $i;done
#for i in {1..10};do date;sleep 1;done
for i in "123abc":
    print i,

for ch in ['ma','xiao','lang']:
    print ch,

range(10,1,-1)
for i in range(3):
    print "hello world!"

#打印列表下表和值
alist=['alice','whilte','cristin']
# for i in alist:
#     pritn i

for i in range(len(alist)):
    print i,":",alist[i]

#xrange
for i in xrange(100000):
    print i,

# 列表生成器
[ i**2 for i in range(10) ]

[ i**2 for i in range(10) if i%2 == 0 ]

