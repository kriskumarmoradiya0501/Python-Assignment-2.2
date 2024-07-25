# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:39:09 2024

@author: 8student6
"""

str = input("Enter String : ")

for i in range(len(str)):
    if(str[i]=='a' or str[i]=='o' or str[i]=='e' or str[i]=='i' or str[i]=='u' or str[i]=='A' or str[i]=='O' or str[i]=='E' or str[i]=='I' or str[i]=='U'):
        print("index of ",str[i]," is ",i)
        
        