#!/usr/bin/python3
# -*- coding: utf-8 -*-
# **********************************************
# Author: xuekaixin
# Mail: jinweiayy@gmail.com
# Website: www.xuejinwei.com
# Date: 2018-04-20 02:46
# Filename: 3-4.py
# Description: 
# Applicable:
# **********************************************
#
name = ["guomi","xuejinwei","xueyanping","zhangfengmei","xuejingfang"]
print("%s,%s,%s,%s, Dinner with me." %(name[0],name[1],name[2],name[3]))
delName = name.pop(0)
print("%s Can't join." % (delName))
#print(name)
name.insert(0,"xuejingna")
print(name)
name.insert(0,"guomi")
name.insert(2,"nainai")
name.append("yeye")
print(name)
