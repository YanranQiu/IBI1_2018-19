# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:06:34 2019

@author: alvaq
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all susceptible population
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')
beta=0.3
gamma=0.05
#find infected points
InfectedIndex=np.where(population==1)
#loop through all infected points
for i in range(len(InfectedIndex[0])):
    # get x, y coordinates for each point
    x = InfectedIndex[0][i]
    y = InfectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (necessary?)
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour!=-1 and yNeighbour!=-1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                        #recovery
                        if population[xNeighbour,yNeighbour]==2:
                            



