# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:43:28 2019

@author: alvaq
"""

#start with a number no larger than 8192
x=2019
#set the power counter k
k=13
#set the loop
while 1==1:
    if (x-2**k)<0:
        k=k-1
        continue
    elif (x-2**k)>=0:
        print( "2**", k, "+") 
        x=x-2**k
        list.append(k)
        k=k-1
        continue
#print the final result
print("2019 is ", )