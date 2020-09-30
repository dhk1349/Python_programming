# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:08:34 2020

@author: dhk13
"""
import numpy as np

def partial_1(x):
    return 4*x[0]+3*x[1]-4

def partial_2(x):
    return 3*x[0]+4*x[1]+2

x0=np.array([1,0.9])

iter_list=x0

g=np.array([])
lr=0.1


for _ in range(100):
    g=(partial_1(iter_list)+partial_2(iter_list))/2
    print(g)
    iter_list=iter_list-lr*g
    print(iter_list)