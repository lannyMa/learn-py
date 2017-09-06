#!/usr/bin/env python
# coding=utf-8
import os

import cPickle

fname = "demo_txl.db"
txl = []


def menu():
    print '''
    0 txl_exit
    1 txl_add
    2 txl_del
    3 txl_update
    4 txl_search
    5 txl_showall
    6 txl_sort
    '''
    op = raw_input("choose one(1,2,3) > ").strip()
    return op


def txl_exit():
    '''退出程序'''
    print "goodbye!!!"
    os._exit(0)


def txl_add():
    '''添加用户'''
    name = raw_input("name: ")
    age = raw_input("age: ")
    gender = raw_input("gender: ")
    tel = raw_input("tel: ")
    tmp = {
        'name': name,
        'age': age,
        'gender': gender,
        'tel': tel,
    }
    txl.append(tmp)
    txl_save()
    print """txl_add user sccessful..."""


def txl_display():
    '''显示所有用户'''
    txl_display_format(txl)


def txl_display_format(txl):
    '''格式化显示工具'''
    if len(txl) > 0:
        print "name\tage\tgender\ttel"
        print "--------------------------------"
        for line in txl:
            print "%(name)s \t %(age)s \t %(gender)s \t %(tel)s \t " % line
    else:
        print "no any user"


def txl_del():
    '''删除数据'''
    flag = 0
    name = raw_input("name you want to del: ").strip()
    for line in txl:
        if line['name'] == name:
            txl.remove(line)
            flag = 1
            break
    else:
        print 'user not exists'
    if flag:
        print "txl_del user sccessful..."
    txl_save()

def txl_save():
    '''保存数据到文件'''
    s = cPickle.dumps(txl)
    with open(fname, 'w') as f:
        f.write(s)


def txl_load():
    '''从文件中读取用户信息'''
    with open(fname) as f:
        s = f.read()
    global txl
    txl = cPickle.loads(s)


def txl_update():
    '''更新用户'''
    flag = 0
    name = raw_input("the name you want to update > ")
    for line in txl:
        if line['name'] == name:
            old_name = name
            old_age = line['age']
            old_gender = line['gender']
            old_tel = line['tel']
            txl.remove(line)
            flag = 1
            break
    else:
        print " user is not exsis"
        os._exit(0)
    new_name = name
    new_age=raw_input('age: ')
    new_gender = raw_input('gender: ')
    new_tel = raw_input('tel: ')
    # 重新组合用户信息后插入
    tmp = {}
    tmp['name']= new_name
    if new_age:
        tmp['age'] = new_age
    else:
        tmp['age'] = old_age
    if new_gender:
        tmp['gender'] = new_gender
    else:
        tmp['gender'] = old_gender
    if new_tel:
        tmp['tel'] = new_tel
    else:
        tmp['tel'] = old_tel
    txl.append(tmp)
    txl_save()
    if flag:
        print "update user info successful"

def txl_search():
    name = raw_input("the name you want to search> ")
    for line in txl:
        txl_display_format([line])


def txl_sort():
    '''根据用户输入的排序'''
    op = raw_input("name | age | gender | tel | Display >>>")
    txl.sort(key=lambda x:x[op])
    txl_display()

ops = {
    '0': txl_exit,
    '1': txl_add,
    '2': txl_del,
    '3': txl_update,
    '4': txl_search,
    '5': txl_display,
    '6': txl_sort,
}


def main():
    while True:
        op = menu()
        if op in '0123456':
            ops.get(op, txl_exit)()


txl_load()

if __name__ == '__main__':
    main()
