# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:52:59 2020

@author: admin
"""

list1=[1,2,3,4,5]
list2=[6,7,8,9,2]

def getPairs(sum):
    sum=7
    count=0
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i]+list2[j]==sum:
                count=count+1
                print(list1[i],list2[j])
    return count
print("count pairs is",getPairs(sum)) 
            