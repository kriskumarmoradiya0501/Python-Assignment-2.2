# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:49:22 2024

@author: 8student6
"""

digit = 0
letter = 0
special = 0
str = input("Enter String : ")

for i in str:
    if (i.isalpha()):
        letter = letter+1
    elif(i.isdigit()):
        digit = digit+1
    else:
        special = special+1
        
print("Digit = ",digit)
print("Letters = ",letter)
print("Special = ",special)
