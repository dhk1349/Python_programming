# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:03:53 2020

@author: dhk1349
"""

#enuimerator

a="1"
b="2"
c="3"
a,b,c=map(lambda x:x if type(x)==list else [x], (a,b,c))

print(a,b,c)