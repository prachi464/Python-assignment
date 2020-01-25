# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:56:28 2020

@author: admin
"""
from array import array
def getPairs(arr,n,sum):
    count=0
    
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==sum:
                count+=1
                print(arr[i],arr[j])
    return count
arr=array('i',[1,5,2,4])
n=len(arr)
sum=6
print("count pairs is",getPairs(arr,n,sum)) 
