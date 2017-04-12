#!/usr/bin/env python
# coding=utf-8

import random

ch_list = {
    0: '石头',
    1: '剪刀',
    2: '布'
}

# menu
op = '''
0, 选石头
1, 选剪刀
2, 选布
请选一项(0/1/2) > '''
pc_op = random.choice([0, 1, 2])
# people_op = int(raw_input(op))
while True:
    people_op = int(raw_input(op))
    if people_op in [0, 1, 2]:
        break

# print result
print '''
你选的是:   %s
电脑选的是: %s
''' % (ch_list.get(people_op), ch_list.get(pc_op))

win_list = [[1, 0], [2, 0], [2, 1]]

if [people_op, pc_op] in win_list:
    print '恭喜你,你赢了.'
elif people_op == pc_op:
    print '平局!'
else:
    print '电脑赢了!'
