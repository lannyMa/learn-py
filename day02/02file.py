#!/usr/bin/env python
# coding=utf-8

# f=open('file.txt','r')
# data=f.read()
# print data,type(data)
#
# for line in f:
#     print f.readlines()
# f.close()

f=open('file2.txt','w')
f.write("1nd maxiaolang\n")

# f.read        字符串
# f.readline    字符串
# f.readlines   列表  对应writelines

f.writelines(['2nd lines\n','3nd lines\n',])
f.flush()
f.close()