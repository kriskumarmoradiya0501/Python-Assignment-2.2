# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:48:51 2024

@author: 8student6
"""

str= input("Enter String : ")
str1 = input("Enter String 2 : ")
count = 0
for i,j in zip(str,str1):
    if(i==j):
        count = count+1
        
        
if count > 1:
    print("It has common prefix.")
else:
    print("It not has common prefix.")