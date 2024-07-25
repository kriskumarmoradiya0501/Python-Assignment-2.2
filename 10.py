# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:14:55 2024

@author: 8student6
"""


i = 0
while i < 3:
    str = input("Enter String : ")
    if(str == "Admin"):
        print("Access Granted .")
        break
    else:
        print("Pass is not valid")
    i=i+1
    