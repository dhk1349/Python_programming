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
    print(len(inputlist))
    print(inputlist)
        

        
if __name__=="__main__":
    """
    inputlist=[(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)]
    buf=BufferCache(3)
    buf.Initialize(inputlist)
    buf.SearchHash(11)
    """
    RandomInputGenerator()

    