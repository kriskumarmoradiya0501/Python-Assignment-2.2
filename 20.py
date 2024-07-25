# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:18:30 2024

@author: 8student6
"""

f = 0
m = 0
str = input("Enter String : ")
c  = str[0]

for i in range(len(str)):
    for j in range(i+1,len(str)):
        if (str[i]==str[j]):
            f = f+1
    if(f > m):
        temp = f
        f = m
        m = f
        c=str[i]

print("Most frequant char is = ",c)