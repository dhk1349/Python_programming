#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:12:23 2019

@author: donghoon

Scenario
#1 Requesting block that is in the freelist and queue
#2 Requesting block that is not in the queque and freelist
#3 Requesting block that is not in the queque and freelist but free block is in delayed write
#4 Requesting block that is not in the queque and freelist no free block left
#5 Requesting block but block is in use
"""

import random
import math
from BufferModule import *

def RandomInputGenerator():
    processnum=random.randrange(3, 101)
    temp=set()
    while len(temp)!=processnum:
        temp.add(random.randrange(1,500))
    temp=list(temp)
    inputlist=[]
    for i in temp:
        #change time into log scale calculation
        inputlist.append((i,10-math.floor(math.log(random.randrange(1,3000),2))))
    #print(len(inputlist))
    #print(inputlist)
    return inputlist
        
def BufferCacheModel():
    print("\t==================")
    print("\t1. Scenario 1")
    print("\t2. Scenario 2")
    print("\t3. Scenario 3")
    print("\t4. Scenario 4")
    print("\t5. Scenario 5")
    print("\t6. User Input")
    print("\t7. Randomly Generate Input")
    print("\t8. EXIT")
    print("\t==================")
    option=input("\tChoose option: ")
    print()
    if (ord(option)>=49 and ord(option)<=53):
        inputs=[
        [(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)], #S1, S2
        [(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)], #S1, S2
        [(10,1),(5,-1), (3,1), (11,0), (6,0), (8, 1)], #S3
        [(10,2),(5,2), (3,3), (11,5), (6,3), (8, 5)], #S4
        [(10,2),(5,2), (3,0), (11,5), (6,3), (8, 5)]] #S5
        buf=BufferCache(3)
        buf.Initialize(inputs[ord(option)-49])
        buf.PrintAll()
        
        Getblklist=[11, 1, 1, 1, 10]
        buf.GetBlock(Getblklist[ord(option)-49])
        buf.PrintAll()
        
    elif ord(option)==54:
        print("user input mode")
        temp=input("Tpye input: ")
        temp=temp.split()
        inputlist=[]
        for i in range(0,len(temp),2):
            inputlist.append((int(temp[i]), int(temp[i+1])))
        modnum=int(input("Type mod number: "))
        req=int(input("What will you request? "))
        
        buf=BufferCache(modnum)
        buf.Initialize(inputlist)
        buf.PrintAll()
        
        buf.GetBlock(req)
        buf.PrintAll()
        
    
    elif ord(option)==55:
        print("Randomly Generating inputs...(3-100 processes)")
        inputs=RandomInputGenerator()
        buf=BufferCache(random.randrange(4, 10))
        buf.Initialize(inputs)
        buf.PrintAll()
        
        Getblklist=[]
        for i in inputs:
            Getblklist.append(i[0])
        for i in range(len(inputs)):
            Getblklist.append(random.randrange(1,500))
        
        buf.GetBlock(Getblklist[random.randrange(0,len(Getblklist))])
        buf.PrintAll()
        
    elif ord(option)==56:
        print("EXITING PROGRAM")
        return
    else:
        print("Illegal input")
        return
        
if __name__=="__main__":
    """
    inputlist=[(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)]
    buf=BufferCache(3)
    buf.Initialize(inputlist)
    buf.SearchHash(11)
    """
    #RandomInputGenerator()
    while True:
        BufferCacheModel()

    