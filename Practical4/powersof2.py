# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:43:28 2019

@author: alvaq
"""

#start with a number no larger than 8192
x=2019
#set k as the exponent
k=0
#set the cumulative result
r=str(x)+" is "
#set the loop
while x>0:
    a=1
    while a<=x:
        a=a*2
        k=k+1
    k=k-1
    print("2**"+str(k))
    x=x-a/2
    if r!=0:
        r=r+"2**"+str(k)+"+"
    else:
        r=r+"2**"+str(k)
#print the final result
print(r)