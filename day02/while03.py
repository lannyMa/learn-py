#!/usr/bin/env python
# coding=utf-8


sum = 0
counter = 0

while counter <= 100:
    if not counter%2:
    # if counter%2==0:
        # continue
        sum += counter
    counter += 1


#循环正常结束,会执行else
else:
    print 'the end'
print sum
# while counter <= 100:
#     counter += 1
#     #if counter % 2 == 1:
#     if counter % 2: #简单化 布尔类型
#         continue
#     sum += counter
#
# print sum
