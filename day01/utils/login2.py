#!/usr/bin/env python
# coding=utf-8

import getpass
username=raw_input('username: ')
password=getpass.getpass('password: ')

if username=='bob' and password=='123456':
    print 'login suceess!!!'
else:
    print 'failed'