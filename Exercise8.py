#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Zongzake Buaparot 362515241019 EE36241N
'''
usernameinput = input("username :") 
passwordinput = input("password:") 
if usernameinput=="Zongzake" and passwordinput =="792665": 
    print("Welcome to Zongzake Shop") 
    print("What do want to buy something?") 
    print("This is all Menu in Zongzake Shop") 
    print("-----------------------------------------") 
    print("1.Banana 15 THB") 
    print("2.Water 10 THB") 
    print("3.Noodle 40 THB") 
    print("4.Rice 150 THB") 
    print("5.Buns 12 THB") 
    print("-------------------") 
    Item=int(input("Do you want to buy? ")) 
    
    if Item==1: 
        cost1=15 
        print("Your Item:",Item," = ",cost1,"THB") 
    elif Item==2: 
        cost1=10 
        print("Your Item:",Item," = ",cost1,"THB") 
    elif Item==3: 
        cost1=40 
        print("Your Item:",Item," = ",cost1,"THB") 
    elif Item==4: 
        cost1=150 
        print("Your Item:",Item," = ",cost1,"THB") 
    elif Item==5: 
        cost1=12 
        print("Your Item:",Item," = ",cost1,"THB") 
    amount1 =int(input("Do you want to amount? ")) 
    
    if Item==1: 
        cost1=15 
        print("Total:",Item," = ",cost1*amount1,"THB") 
    elif Item==2: 
        cost1=10 
        print("Total:",Item," = ",cost1*amount1,"THB") 
    elif Item==3: 
        cost1=40 
        print("Total:",Item," = ",cost1*amount1,"THB") 
    elif Item==4: 
        cost1=150 
        print("Total:",Item," = ",cost1*amount1,"THB")
    elif Item==5: 
        cost1=12 
        print("Total:",Item," = ",cost1*amount1,"THB") 
    Item=int(input("Do you want to buy? ")) 
        
    if Item==1: 
        cost2=15 
        print("Your Item:",Item," = ",cost2,"THB") 
    elif Item==2: 
        cost2=10 
        print("Your Item:",Item," = ",cost2,"THB") 
    elif Item==3: 
        cost2=40 
        print("Your Item:",Item," = ",cost2,"THB") 
    elif Item==4: 
        cost2=150 
        print("Your Item:",Item," = ",cost2,"THB") 
    elif Item==5: 
        cost2=12 
        print("Your Item:",Item," = ",cost2,"THB") 
    amount2 =int(input("Do you want to amount? ")) 

    if Item==1: 
        cost2=15 
        print("Total:",Item," = ",cost2*amount2,"THB") 
    elif Item==2: 
        cost2=10 
        print("Total:",Item," = ",cost2*amount2,"THB") 
    elif Item==3: 
        cost2=40 
        print("Total:",Item," = ",cost2*amount2,"THB") 
    elif Item==4: 
        cost2=150 
        print("Total:",Item," = ",cost2*amount2,"THB") 
    elif Item==5: 
        cost2=12 
        print("Total:",Item," = ",cost2*amount2,"THB")
    Item=int(input("Do you want to buy? ")) 
    
    if Item==1: 
        cost3=15 
        print("Your Item:",Item," = ",cost3,"THB") 
    elif Item==2: 
        cost3=10 
        print("Your Item:",Item," = ",cost3,"THB") 
    elif Item==3: 
        cost3=40 
        print("Your Item:",Item," = ",cost3,"THB") 
    elif Item==4: 
        cost3=150 
        print("Your Item:",Item," = ",cost3,"THB") 
    elif Item==5: 
        cost3=12 
        print("Your Item:",Item," = ",cost3,"THB") 
    amount3 =int(input("Do you want to amount? ")) 
    
    if Item==1: 
        cost3=15 
        print("Total:",Item," = ",cost3*amount3,"THB") 
    elif Item==2: 
        cost3=10 
        print("Total:",Item," = ",cost3*amount3,"THB") 
    elif Item==3: 
        cost3=40 
        print("Total:",Item," = ",cost3*amount3,"THB") 
    elif Item==4: 
        cost3=150 
        print("Total:",Item," = ",cost3*amount3,"THB") 
    elif Item==5: 
        cost3=12 
        print("Total:",Item," = ",cost3*amount3,"THB") 
    print("All Total=",cost1*amount1+cost2*amount2+cost3*amount3,"THB") 
else: 
    print("Error") 


# In[ ]:




