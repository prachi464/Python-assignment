# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:04:09 2020

@author: admin
"""

string=input("Enter any string with lower and upper string character")
string1=""
string2=""
for i in range(len(string)):
    if string[i].islower():
        string1=string1+string[i]
    elif string[i].isupper():
        string2=string2+string[i]
print(string1+string2)