#!/usr/bin/python3
# -*- coding: utf-8 -*
#
# **********************************************
# Author: xuekaixin
# Mail: jinweiayy@gmail.com
# Website: www.xuejinwei.com
# Date: 2018-06-06 16:43
# Filename: 6-2.py
# Description: 
# Applicable:
# **********************************************
#
digitals = {
	"a":"1",
	"b":"2",
	"c":"3",
	"d":"4",
	"e":"4",
	"f":"2",
	}

print(digitals)

for digitalsKey in sorted(digitals.keys()):
	print(digitalsKey)

for digitalsValues in set(sorted(digitals.values())):
	print(digitalsValues)
