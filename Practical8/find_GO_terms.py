# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:10:19 2019

@author: alvaq
"""

#import libraries
import xml.dom.minidom
import re
import pandas as pd

#access files
fpath=input("Please input the file path:\n")
fname='go_obo.xml';
resName='autophagosome.xlsx'
go_obo=fpath+'/'+fname
res=fpath+'/'+resName

#precompile go term
re_immu=re.compile(r'autophagosome')

#define function to find childnodes 
def Childnodes(id, resultSet):
    for t in go:
        parents=t.getElementsByTagName('is_a')
        geneid=t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            #add children gene ids
            if parent.childNodes[0].data==id:
                resultSet.add(geneid)
                #stop when all childnodes are covered
                Childnodes(geneid, resultSet)
                
#create a pandas.Dataframe to store the output
df=pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree    
DOMTree=xml.dom.minidom.parse(go_obo) 
obo=DOMTree.documentElement
go=obo.getElementsByTagName('term')
for term in go:
    defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms defined with "autophagosome"
    if re_immu.search(defstr):
        id=term.getElementsByTagName('id')[0].childNodes[0].data
        name=term.getElementsByTagName('name')[0].childNodes[0].data
        resultSet=set()
        Childnodes(id, resultSet)
        df=df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]})) 
        print(id, len(resultSet))
#save to excel
df.to_excel(res,index=False)
