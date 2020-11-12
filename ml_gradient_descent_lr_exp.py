# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:32:07 2020

@author: dhk13
"""
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

x_data = [1.0, 2.0, 3.0] 
y_data = [2.0, 4.0, 6.0] 
w = 1.0 # a random guess: random value 
lr = 0.1 # learning rate 
# our model forward pass 
lr_exp_org=np.array([0.01, 0.1, 1, 100])
lr_exp=np.array([0.01, 0.1, 1, 100])

w_result=defaultdict(list)
loss_result=defaultdict(list)

def forward(x): 
    return x * w 

# Loss function 
def loss(x, y): 
    y_pred = forward(x) 
    return (y_pred - y) * (y_pred - y) 


# compute gradient
def gradient(x, y): # d_loss/d_w 
    return 2 * x * (x * w - y) 
    
# Before training 
print("predict (before training)", 4, forward(4)) 

for i in range(len(lr_exp)):
        w_result[i].append(lr_exp[i])

# Training loop 
for epoch in range(10): 
    for x_val, y_val in zip(x_data, y_data): 
        grad = gradient(x_val, y_val) 
        w = w - lr_exp * grad 
        print("\tgrad: ", x_val, y_val, np.round(grad, 4)) 
        l = loss(x_val, y_val) 
        
    for i in range(len(lr_exp)):
        w_result[i].append(lr_exp[i])
        loss_result[i].append(l[i])
    
    print("progress:", epoch, "w=", np.round(w, 4), "loss=", np.round(l, 4)) 
    
# After training 
print("predict (after training)", "4 hours", forward(4))


epoch=[i for i in range(11)]

fig=plt.figure()

w_graph=fig.add_subplot(1,2,1)
loss_graph=fig.add_subplot(1,2,2)

for i in range(4):
    w_graph.plot(epoch, w_result[i], label=lr_exp_org[i])
 
for i in range(4):
    loss_graph.plot(epoch[1:], loss_result[i], label=lr_exp_org[i])

w_graph.set_ylabel('w')
w_graph.set_xlabel('epochs')
loss_graph.set_ylabel('loss')
loss_graph.set_xlabel('epochs')
#loss_graph.set_ylim(0,10)
plt.legend(fontsize='x-large')
plt.show()