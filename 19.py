# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:54:22 2024

@author: 8student6
"""

str = input("Enter String : ")
flag = 0
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if(str[i]==str[j]):
            flag = 0
            break;
        else:
            flag = 1
            
if (flag==0):
    print("String is no unique : ")
else:
    print("String is unique.")
    
