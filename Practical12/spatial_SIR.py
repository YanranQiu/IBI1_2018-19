# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:06:34 2019

@author: alvaq
"""

#import libraries
import numpy as np 
import matplotlib.pyplot as plt

#set up parameters
beta=0.3
gamma=0.05

#make array of all susceptible population
population=np.zeros((100 , 100))

#randomly choose the outbreak point and plot it
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150) 
plt.imshow(population,cmap='viridis',interpolation='nearest')

#find the outbreak point
outbreakP=np.where(population==1)
xL=outbreakP[0]
yL=outbreakP[1]

#loop in range(100)
for j in range(100):
    #loop through all infected places
    for i in range(len(xL)): 
        #get x, y coordinates for each point
        x=xL[i]
        y=yL[i]
        #find the neighbour 
        for xneighbour in range(x-1,x+2):
            for yneighbour in range(y-1,y+2):
                #a person does not infect themselves
                if (xneighbour,yneighbour)!=(x,y):
                    #the neighbour is within the range 
                    if xneighbour!=-1 and yneighbour!=-1 and xneighbour!=100 and yneighbour!=100:
                        #randomly infect susceptible people
                        if population[xneighbour,yneighbour]==0:
                            population[xneighbour,yneighbour]=np.random.choice(range(2),1,p=[1-beta,beta])
                            if population[xneighbour,yneighbour]==1:
                                xneighbour=np.array([xneighbour])
                                yneighbour=np.array(yneighbour) 
                                #add newly infected location to the array
                                xL=np.append(xL,xneighbour)
                                yL=np.append(yL,yneighbour)
                        if population[xneighbour,yneighbour]==1:
                            #randomly recover people, assign 2 for recovered people
                            population[xneighbour,yneighbour]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
                                         
    #show the figure at specific points
    if j in [0,10,20,30,40,50,60,70,80,90,100]:
        plt.figure(figsize=(6,4),dpi=150) 
        plt.imshow(population,cmap='viridis',interpolation='nearest')
