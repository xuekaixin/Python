#!/usr/bin/python3
# -*- coding: utf-8 -*
#
# **********************************************
# Author: xuekaixin
# Mail: jinweiayy@gmail.com
# Website: www.xuejinwei.com
# Date: 2018-06-06 11:37
# Filename: books.py
# Description: 
# Applicable:
# **********************************************
#
dict1 = {"book1":"The World According to Garp","book2":"he Bridge of San Luis Rey","book3":"Alice Sebold"}

print(dict1["book1"])
print(dict1["book2"])
print(dict1)

dict1["book4"] = "cle Bones"
print(dict1)

dict2 = {}
dict2["author"] = "Peter Hessler"
dict2["Publisher"] = "Harper Perennial"
print(dict2)

dict3 = {"author":"Peter Hessler"}
print(dict3)
dict3["author"] = "Alice Sebold"
print(dict3)

dict4 = {"book1":"The World According to Garp","book2":"he Bridge of San Luis Rey","book3":"Alice Sebold"}
print(dict4)
del dict4["book1"]
print(dict4)
