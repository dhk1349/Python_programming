# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:26:18 2020

@author: dhk1349
"""

#Yield practice
print("life is short, art is long")
print("So we should use python")

inputlist=[(0,'a'),(1,'b'),(2,'c'),(3,'d'),(4,'e')]
def yieldfnc(gen):
    for i,j in gen:
        if i%2==0:
            yield j
            

for i in yieldfnc(inputlist):
    print (i)