# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:01:53 2019

@author: alvaq
"""

#input sequences
SOD2_human_seq="MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
SOD2_mouse_seq="MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
random_seq="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"

#read BLOSUM62 matrix
from Bio.SubsMat import MatrixInfo
BLOSUM62=MatrixInfo.blosum62

#build dictionary of BLOSUM62 matrix
keys=list(BLOSUM62.keys())
values=list(BLOSUM62.values())

#define function for assigning scores
def blosum(a,b):
    if (a,b) in keys:
        index=keys.index((a,b))
        score=values[index]
    elif (b,a) in keys:
        index=keys.index((b,a))
        score=values[index]
    return score

#compare human seq with mouse seq
scr1=0 #varialbe for BLOSUM score
perc1=0 #variable for percentage identity
for i in range(len(SOD2_human_seq)):
    scr=blosum(SOD2_human_seq[i],SOD2_mouse_seq[i])
    if SOD2_human_seq[i]==SOD2_mouse_seq[i]:
        perc1+=1
    scr1=scr1+scr
    perc_1=perc1/len(SOD2_human_seq)

#compare human seq with random seq
scr2=0
perc2=0
for i in range(len(SOD2_human_seq)):
    scr=blosum(SOD2_human_seq[i],random_seq[i])
    if SOD2_human_seq[i]==random_seq[i]:
        perc2+=1
    scr2=scr2+scr
    perc_2=perc2/len(SOD2_human_seq)

#compare mouse seq with random seq
scr3=0
perc3=0
for i in range(len(random_seq)):
    scr=blosum(random_seq[i],SOD2_mouse_seq[i])
    if SOD2_mouse_seq[i]==random_seq[i]:
        perc3+=1
    scr3=scr3+scr
    perc_3=perc3/len(random_seq)
    
#bonus project (graphical alignment)
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
for a in pairwise2.align.globaldx(SOD2_human_seq, SOD2_mouse_seq, BLOSUM62):
    print(format_alignment(*a))
for a in pairwise2.align.globaldx(SOD2_human_seq, random_seq, BLOSUM62):
    print(format_alignment(*a))
for a in pairwise2.align.globaldx(SOD2_mouse_seq, random_seq, BLOSUM62):
    print(format_alignment(*a))

#normalize BLOSUM score
nscr1=scr1/len(SOD2_human_seq)
nscr2=scr2/len(SOD2_human_seq)
nscr3=scr3/len(random_seq)

#print out the analyzed sequences and the final BLOSUM score
print("The final BLOSUM score for human and mouse is "+str(scr1)+".\nThe final BLOSUM score for human and random is "+str(scr2)+".\nThe final BLOSUM score for mouse and random is "+str(scr3)+".")
print("The normalized BLOSUM score for human and mouse is "+str(nscr1)+".\nThe normalized BLOSUM score for human and random is "+str(nscr2)+".\nThe normalized BLOSUM score for mouse and random is "+str(nscr3)+".")
#print out the percentage identity
print("The percentage identity for human and mouse is "+str(perc_1)+".\n"+"The percentage identity for human and random is "+str(perc_2)+".\n"+"The percentage identity for mouse and random is "+str(perc_3)+".")
