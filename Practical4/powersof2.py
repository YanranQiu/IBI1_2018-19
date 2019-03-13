# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:43:28 2019

@author: alvaq
"""

#start with a number no larger than 8192
x=int(input())
#set the cumulative result
r=str(x)+" is "
#set the loop
while x>0:
    a=2**0
#set k as the exponent
    k=0
#find the biggest exponent
    while a<=x:
        a=a*2
        k=k+1
#print the exponent in the result and refresh x
    k=k-1
    x=x-a/2
    if r!=0:
        r=r+"2**"+str(k)+"+"
#remove the "+" at the end of the result
r1=r[:-1]
#print the final result
print(r1)