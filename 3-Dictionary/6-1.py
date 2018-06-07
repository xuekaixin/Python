#!/usr/bin/python3
# -*- coding: utf-8 -*
#
# **********************************************
# Author: xuekaixin
# Mail: jinweiayy@gmail.com
# Website: www.xuejinwei.com
# Date: 2018-06-06 15:27
# Filename: 6-1.py
# Description: 
# Applicable:
# **********************************************
#
information = {
	"name": "xiao li",
	"age": "18",
	"height": "50",
	}
print(information)

# for informationKey,informationValue in information.items():
# 	print(informationKey + ":" + informationValue)
# 
# for informationKey in information.keys():
# 	print(informationKey)

element = ["name","age"]
for informationKey in information.keys():
	print(informationKey.title())
	if informationKey in element:
		print("Hello " + informationKey)
