# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:41:49 2019

@author: dhk13
"""
class obj:
    def __init__(self):
        self.number=10
        print("Constructor called")
        
    def pushnumber(self,num):
        self.number=num
        
    def getnumber(self):
        print (self.number)

tempobj=obj()
tempobj.getnumber()

templist=[]
for i in range(10):
    templist.append(obj())
    
for i in range(10):
    templist[i].pushnumber(i)
    
for i in range(10):
    templist[i].getnumber()