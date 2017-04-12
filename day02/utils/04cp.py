#!/usr/bin/env python
# coding=utf-8

'''file 实现cp

/bin/ls拷贝到/root/ls下
每次读4096字节
'''

# sfname=
# dfname=

src_fobj=open('/etc/hosts')
dst_fobj=open("/root/hosts",'w')
while True:
    data=f.read(4096)
    # if f_obj:
    #     new_file.write(f_obj)
    # else:
    #     break
    if not data:
        break
    dfname.write(data)
f.close()
new_file.close()