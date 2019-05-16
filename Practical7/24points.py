# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:05:13 2019

@author: alvaq
"""

#import libraries
import re
from fractions import Fraction

#precompile: the input numbers must be interger between 1 and 23
re_numbertest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
#check numbers till all numbers input are intergers between 1 and 23
i=1
while i:
    i=0
    data=input("Please input the numbers:(use \",\" to divide them)\n")
    numL=data.split(",")
    for char in numL:
        if re_numbertest.match(char): 
            continue
        else: 
            print("The input number must be intergers from 1 to 23")
            i=1
            break

#convert strings into integers
num=list(map(int,numL))

#set counter for recursion times
count=0

#recursion begins!
def dfs(n): #n=len(num), dfs stands for deepfirstsearch
    #count recursion times
    global count
    count+=1
    if n==1:
        #if 24 points can be reached, return 1
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a=num[i]
            b=num[j]
            #eliminate numbers
            num[j]=num[n-1]
            #try +
            num[i]=a+b
            if(dfs(n-1)):
                return 1
            #try -
            num[i]=a-b
            if(dfs(n-1)):
                return 1
            num[i]=b-a
            if(dfs(n-1)): 
                return 1 
            #try *
            num[i]=a*b
            if(dfs(n-1)): 
                return 1
            #try frantion (/), test if the dividend is zero
            if a:
                #floats are not precise
                num[i]=Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 
            if b:
                num[i]=Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            #Backtrack the num list
            num[i]=a
            num[j]=b
    return 0

#print the results
if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)