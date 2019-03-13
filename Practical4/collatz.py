# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:02:08 2019

@author: alvaq
"""
#start with a positive interger
n=6
#repeat the sequence until it reaches 1 for the first time
while n!=1:
#n=n/2 if n is even
    if n%2==0:
        n=n/2
        print (n)
#n=3*n+1 if n is odd
    elif n%2==1 and n!=1:
        n=3*n+1
        print(n)
    else:
        print("n is not an interger")
