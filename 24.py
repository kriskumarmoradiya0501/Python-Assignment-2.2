# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:45:48 2024

@author: 8student6
"""

str= input("Enter String : ")
str1 = input("Enter String 2 : ")
str3 = ""
for i,j in zip(str,str1):
    str3=str3+i+j

print(str3)