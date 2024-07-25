# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:12:47 2024

@author: 8student6
"""


str = input("Enter String : ")
i = 0
while i < len(str):
    if(str[i].isalpha()):
        print(str[i],end=(" "))
    i=i+1
    