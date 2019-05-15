# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:11:37 2019

@author: alvaq
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define the basic variables of the model
susceptible=9999
infected=1
recovered=0
N=10000 #N holds the totoal number of people in the population
beta=0.3
gamma=0.05
#create arrays for variables
tracker=np.array((susceptible,infected,recovered))
# using append() to insert new value at end 
#arr.append(1)
#make list of people
#Use the "choice" function to draw a random number
for i in range(1000):
    proportion=beta*(infected/N)
    new_infected=np.random.choice(range(2),susceptible,p=[1-proportion,proportion])
    new_recovered=np.random.choice(range(1),infected,p=[1-gamma,gamma])
    
    #plot
    plt.figure(figsize=(6,4),dpi =150)
    
plt.show
