# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:16:48 2020

@author: admin
"""

s="English=78 science=83 math=68 history=65"
strn=s.split(" ")
print(strn)
sum=0;
for i in range(0,len(strn)):
    a=strn[i].split("=")
    print(a)
    for j in a:
        if j.isnumeric():
            print(j)
            sum=sum+int(j)
print("sum:",sum)
percentage=(sum*100)/400
print("percentage:",percentage)
