#!/usr/bin/env python
# coding=utf-8
'''fibo数列生成器

fibo数列:每个数总是前2个数的和
'''

fib=[0,1]


# for i in range(10):
#     x=fib[i]+fib[i+1]
#     fib.append(x)
# print fib

# alist[-1] alist[-2]最后两项
# alist.append添加值
num=int(raw_input("Input a num > "))

for i in range(num-2):
    fib.append(fib[-1]+fib[-2])
print fib