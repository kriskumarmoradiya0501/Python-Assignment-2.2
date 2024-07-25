# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:39:09 2024

@author: 8student6
"""


i = 0
count = 0
str = input("Enter Your String : ")
while i < len(str):
    if str[i] in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
        count = count+1
    i = i + 1
print(count)
