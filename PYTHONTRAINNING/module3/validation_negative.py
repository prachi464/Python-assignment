# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:56:59 2020

@author: admin
"""

n=int(input("Enter number of items"))
whole=0
for i in range(0,n):
    while(True):
        print("Enter Price:",i+1)
        a=int(input())
        if a>0:
            whole=whole+a
            break
        else:
            pass
retail=whole*0.5
print("Retail:",retail)