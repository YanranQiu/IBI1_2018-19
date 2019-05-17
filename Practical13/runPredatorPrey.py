# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:01:48 2019

@author: alvaq
"""

#import libraries
import os #access operating system from within python
#os.chdir()
import matplotlib.pyplot as plt
import xml.dom.minidom
import numpy as np
import re

#define function to convert the .xml file into a .cps file in the same directory (provided by Melanie)
def xml_to_cps():
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()


os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
os.system("CopasiSE.exe predator-prey.cps")
resultsl=[]
with open('modelResults.csv', 'r') as cpsfile:
    cpsfile=cpsfile.read()
    cpscontent=re.split('\n',cpsfile)
    #make an array for variable names
    names=np.array(cpscontent[0])
    print(names)
    #resultss=np.array(cpscontent[1:])
    for i in range(1,len(cpscontent)-1):
        results=re.split(',',cpscontent[i])
        resultsl.append(results)
    results=np.array(resultsl)

plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,1],label='predator (b=0.02,d=0.4)')
plt.plot(results[:,2],label='prey (b=0.1,d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend(loc='upper right')

plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,1],results[:,2])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('limit cycle')

#change values
#import xml.dom.minidom
#create a DOMTree




