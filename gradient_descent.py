# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:08:34 2020

@author: dhk13
"""
import numpy as np

def func(x):
    return 2*x[0]**2 + 3*x[0]*x[1] + 2*x[1]**2 -4*x[0]+2*x[1]-24

def partial_1(x):
    return 4*x[0]+3*x[1]-4

def partial_2(x):
    return 3*x[0]+4*x[1]+2

x0=np.array([1,0.9])

min_set=[22/7, -20/7]


iter_list=x0

g=np.array([])
lr=0.1

print("min= ", func(min_set))

for _ in range(10):
    g1=partial_1(iter_list)
    g2=partial_2(iter_list)
    print(g1, g2)
    iter_list[0]=iter_list[0]-lr*g1
    iter_list[1]=iter_list[1]-lr*g2
    
    print(iter_list)
    print("value= ", func(iter_list))