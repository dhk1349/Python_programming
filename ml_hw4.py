# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:29:13 2020

@author: dhk1349
"""
import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0,x)


u1=np.array([[-0.3, 1, 1.2],[1.6, -1, -1.1]])
u2=np.array([[1,1,-1],[0.7,0.5,1]])
u3=np.array([[0.5,-0.8,1],[-0.1,0.3,0.4]])
u4=np.array([[1,0.1,-0.2],[-0.2,1.3,-0.4]])
#u3=np.array([[0.5,-0.8,0.9],[-0.1,0.3,0.4]])


x=np.array([[1],[1],[0]])

print(u1.dot(x))

z1_sig=sigmoid(u1.dot(x))
z1_relu=relu(u1.dot(x))

print(z1_sig, z1_relu)

z1_sig=np.insert(z1_sig, 0, 1, axis=0)
z1_relu=np.insert(z1_relu, 0, 1, axis=0)
print(z1_sig, z1_relu)

z2_sig=sigmoid(u2.dot(z1_sig))
z2_relu=relu(u2.dot(z1_relu))


z2_sig=np.insert(z2_sig, 0, 1, axis=0)
z2_relu=np.insert(z2_relu, 0, 1, axis=0)

print(z2_sig, z2_relu, sep="\n")

z3_sig=sigmoid(u3.dot(z2_sig))
z3_relu=relu(u3.dot(z2_relu))


z3_sig=np.insert(z3_sig, 0, 1, axis=0)
z3_relu=np.insert(z3_relu, 0, 1, axis=0)
print(z3_sig, z3_relu, sep="\n")

z4_sig=sigmoid(u4.dot(z3_sig))
z4_relu=relu(u4.dot(z3_relu))


print(z4_sig, z4_relu, sep="\n")