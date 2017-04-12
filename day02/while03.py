#!/usr/bin/env python
# coding=utf-8


sum = 0
counter = 0

while counter <= 100:
    if counter%2==0:
        # continue
        sum += counter
    counter += 1

print sum


# while counter <= 100:
#     counter += 1
#     if counter % 2 == 1:
#         continue
#     sum += counter
#
# print sum
