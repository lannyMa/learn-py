#!/bin/sh

for ip in 192.168.14.{1..10};do
    ping -c2 $ip >/dev/null 2>&1
#    if [ $? -eq 0 ];then
#        echo "$ip is up"
#    else
#        echo "$ip is down"
#    fi
    [ $? -eq 0 ] && echo "$ip is up" || echo "$ip is down"
done

