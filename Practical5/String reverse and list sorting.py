# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:28:05 2019

@author: alvaq
"""

#input a string
str=input("Input a string: ")
#split the string
str=str.split()
#reverse elements and sort the string
r_str=[x[::-1] for x in str]
s_str=sorted(r_str, reverse=True)
#print the string
print(s_str)