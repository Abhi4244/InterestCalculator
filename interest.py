# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:51:50 2022

@author: Abhinav
"""
def compoundInterest (p,r,t):
    amount= p*(pow((1+r/100), t))
    ci = amount-p
    option= str(input("Do you want amount or CI? --->"))
    if option=="Amount" or option=="amount" or  option=="A" :
        print("Amount is" ,"",amount)
    elif option=="compound" or option=="ci" or option=="CI":
        print("Compound interest is:" ,"",ci)
    else:
        print("Wrong input")
    restart=  str(input("Do you want to restart? --->"))
    if restart=="yes" or restart=="Y" or restart=="Yes" or restart=="y":
        print("Restarting..." ,"...")
        begin()
    elif restart=="no" or restart=="n"  or restart=="N" or restart=="No":
        print("Going to sleep")
    else:
        print("I didn't understand ?")
        
        
        
        
def simpleInterest (p,r,t):
    si = p*r*t/100
    amount=p+si
    option= str(input("Do you want amount or SI? --->"))
    if option=="Amount" or option=="amount" or  option=="A":
        print("Amount is" ,"",amount)
    elif option=="simple" or option=="si" or option=="SI":
        print("Simple interest is:" ,"",si)
    else:
        print("Wrong input")
    restart=  str(input("Do you want to restart? --->"))
    if restart=="yes" or restart=="Y" or restart=="Yes" or restart=="y":
        print("Restarting..." ,"...")
        begin()
    elif restart=="no" or restart=="n"  or restart=="N" or restart=="No":
        print("Going to sleep")
    else:
        print("I didn't understand ?")
    
    
    
def begin():
    p= float(input("Enter the principal amount: "))
    r= float(input("Enter the rate of interest: "))
    t= float(input("Enter the number of years: "))
    option= str(input("Do you want to calculte SI or CI? --->"))
    
    if option=="ci" or option=="CI":
       compoundInterest(p,r,t)
    elif option=="si"  or option=="SI":
       simpleInterest(p,r,t)
    else:
        print("Wrong input")
   

start = begin()

        
        
    
   
    