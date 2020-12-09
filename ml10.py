#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 03:50:41 2020

@author: dhk1349
"""

import numpy as np

def MSE(pred, target):
    return np.mean((pred-target)**2)

def CrossEntropy(pred, target):
    return -np.mean(target*np.log(pred) + (1-target)*np.log(1-pred))

def LogLikely(pred, target):
   for idx, t in enumerate(target):
       if t==1:
           return -np.log2(pred[idx])

pred=np.array([0.001, 0.9, 0.001, 0.098])
Y=np.array([0,0,0,1])

print(MSE(pred, Y))
print(CrossEntropy(pred, Y))
print(LogLikely(pred, Y))




x=np.array([[1,1],[2,3],[3,3]])
y=np.array([3.0, 7.0, 8.8])

def WHat(X, Y, Lambda):
    return np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)+2*Lambda*np.identity(np.shape(X)[-1])),np.matmul(np.transpose(X),Y))

print(WHat(x, y, 0.1))
print(WHat(x, y, 0.5))
#lambda is degree of regularization
#if lambda gets bigger, page 43 limits the size(?) of parameter by pulling parameters more to the origin

