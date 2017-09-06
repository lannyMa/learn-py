#!/usr/bin/env python
# coding=utf-8

'''
实现10以内的加法运算.

'''
from operator import add, sub
from random import choice, randint

ops = {'+': add, '-': sub}


def doprob():
    '''生成算数题目'''
    op = choice("+-")
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops.get(op)(*nums)
    pr = '%d %s %d= ' % (nums[0], op, nums[1])

    num = 0
    while True:
        try:
            if (int(input(pr))) == ans:
                print("correct!")
                break
            if num == 2:
                print("the ans is %s %d" % (pr, ans))
            else:
                print("increct,try again!")
                num += 1
        except(KeyboardInterrupt, EOFError, ValueError):
            print("invalid input ,try again!")


def main():
    while True:
        doprob()
        try:
            opt = input("Again?[y]").lower()
            if opt and opt[0] == "n":
                break
        except(KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
