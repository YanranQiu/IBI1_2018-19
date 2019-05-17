# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:05:55 2019

@author: alvaq
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#loop in range(11)
for j in range(11):
    susceptible=9999
    infected=1
    recovered=0
    N=10000 #N holds the totoal number of people in the population
    beta=0.3
    gamma=0.05
    #different propotions of people get vaccinated
    vaccination=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    #create tracker
    tracker=np.array((infected,susceptible,recovered))
    #loop in range(1000)
    for i in range(1000):
        proportion=beta*(infected/10000)
        #use the "choice" function to draw a random number
        new_infected=np.random.choice(range(2),susceptible-int(N*vaccination[j])+1,p=[1-proportion,proportion])
        new_recovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
        new_infected=sum(new_infected)
        new_recovered=sum(new_recovered)
        infected=infected+new_infected-new_recovered
        susceptible=susceptible-new_infected
        recovered=recovered+new_recovered
        #keep track of changes
        trk_update=np.array((infected,susceptible,recovered))
        tracker=np.append(tracker,trk_update)
    #store plot info
    x=[tracker[i] for i in range(0,len(tracker),3)]
    plt.ylabel('number of people')
    plt.xlabel('time')
    y_pos=np.arange(1000)
    plt.plot(x)
    plt.legend(['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
    plt.title('SIR model')

#show plot
plt.savefig ("SIR_vaccination.png" ,type="png")
plt.show()
