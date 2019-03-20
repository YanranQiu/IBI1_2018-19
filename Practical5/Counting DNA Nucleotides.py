# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:04:16 2019

@author: alvaq
"""

#input a DNA string s of length at most 1000 nucleotides and create a list for it.
s=input("Input a DNA sequence: ")
list_s=list(s)
#set 4 variables storing the numbers of different nucleotides.
a=list_s.count("A")
c=list_s.count("C")
g=list_s.count("G")
t=list_s.count("T")
#set a dictionary for the 4 variables and print it
dna_sequence={'A':a, 'C':c, 'G':g, 'T':t}
print(dna_sequence)
#plot
import matplotlib.pyplot as plt
labels='A', 'C', 'G', 'T'
explode=(0,0,0,0)
sizes=[a,c,g,t]
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()