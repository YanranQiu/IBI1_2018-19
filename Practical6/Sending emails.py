# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:06:02 2019

@author: alvaq
"""

#import libraries
import re
from email.header import Header
import email.mime
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTPException

#prepare files
fpath=input("Please input your file path:\n") #input filepath
addressn='address_information.csv'
addressf=fpath+'/'+addressn #add address file pathway
bodyn='body.txt'
bodyf=fpath+'/'+bodyn #add body file pathway

#re precompile
re_email=re.compile(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')
re_loginname=re.compile(r'(\S+)@')

#verify email address
#read address info
with open(addressf, 'r') as address:
    address=address.read()
#split address info
all=re.split(r'[,\n]',address) 
#create list to store useful info
mList=[]
for i in range(3,13,3):
    mList.append([all[i],all[i+1],all[i+2]])
#create filter list to filter correct addresses
filter_list=mList[0:]
#filter correct addresses and output success or error message
for i in range(0,len(mList)):
    if re_email.match(mList[i][1]): #filter correct addresses and output success message
        print(mList[i][1],': Correct Address!')
    else: #filter wrong addresses, output error message and remove them
        print(mList[i][1],': Wrong Address!')
        filter_list.remove(mList[i])

#send emails
with open(bodyf, 'r') as bodyr:     
    bodyr=bodyr.read()
from_addr=input("From: ")
from_password=input("Password: ")
Your_name=input("Input your name:")
for char in filter_list:
    to_addr=char[1]
    subject=char[2]
    #change salutation for different users
    body=re.sub('User',char[0],bodyr)
    loginname=re_loginname.search(from_addr).group(1)
    from_name=Header(Your_name,'utf-8')
    from_name.append(from_addr,'ascii')
    to_name=Header(char[0],'utf-8')
    to_name.append(to_addr,'ascii')
    msg=MIMEText(body,'plain','utf-8')
    msg['From']=from_name
    msg['To']=to_name
    msg['Subject']=Header(subject,'utf-8')
    try:
        server=smtplib.SMTP('smtp.zju.edu.cn',25)
        server.login(loginname,from_password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('Mail sent successfully!')
    except smtplib.SMTPException:
        print('Mail delivery failed')