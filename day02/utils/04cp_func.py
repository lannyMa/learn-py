#!/usr/bin/env python
# coding=utf-8

'''file 函数实现cp


'''
import sys
# sfname=
# dfname=

#位置参数 print sys.argv
src=sys.argv[1]
dst=sys.argv[2]

def cp(sfname,dfname):
    src_fobj=open(sfname)
    dst_fobj=open(dfname,'w')
    while True:
        data=src_fobj.read(4096)
        # if f_obj:
        #     new_file.write(f_obj)
        # else:
        #     break
        if not data:
            break
        dst_fobj.write(data)
    src_fobj.close()
    dst_fobj.close()

# cp(sys.argv[1],sys.argv[2])
cp(src,dst)