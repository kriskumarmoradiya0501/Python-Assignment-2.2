# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:18:42 2024

@author: 8student6
"""
atm = 50000
while True : 
    print("If you want to deposit the money than enter 1 \n if you want to withdraw enter 2\n if you want to end the task enter 3.")
    n = int(input("Enter Your choice : "))
    if(n==1):
        a = int(input("Enter Your Amount of deposit : "))
        atm=atm+a
    elif(n==2):
        a = int(input("Enter Your Amount of withdraw : "))
        if(a>atm):
            print("Not sufficiant Balance in ATM")
        else:
            atm=atm-a
    elif(n==3):
        print("exit")
        break;
    else:
        print("Invalid input")