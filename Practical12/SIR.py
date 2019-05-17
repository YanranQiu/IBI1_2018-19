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

#loop in range(1000)
for i in range(1000):
    proportion=beta*(infected/N)
    #use the "choice" function to draw a random number
    new_infected=np.random.choice(range(2),susceptible,p=[1-proportion,proportion])
    new_recovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
    new_infected=sum(new_infected)
    new_recovered=sum(new_recovered)
    infected=infected+new_infected-new_recovered
    susceptible=susceptible-new_infected
    recovered+=new_recovered
    #keep track of changes
    trk_update=np.array((susceptible,infected,recovered))
    tracker=np.append(tracker,trk_update)
    
#plot
x=[tracker[i:i+3] for i in range(0,len(tracker),3)]
plt.ylabel('number of people')
plt.xlabel('time')
y_pos=np.arange(1000)
plt.plot(x)
plt.legend(['susceptible','infected','recovered'])
plt.title('SIR model')
plt.savefig ("SIR.png" ,type="png")
plt.show() 
