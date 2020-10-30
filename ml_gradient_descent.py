# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:32:07 2020

@author: dhk13
"""
import matplotlib.pyplot as plt


x_data = [1.0, 2.0, 3.0] 
y_data = [2.0, 4.0, 6.0] 
w = 1.0 # a random guess: random value 
lr = 0.1 # learning rate 
# our model forward pass 

w_exp=[0.01, 0.1, 1, 100]

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

# Training loop 
for epoch in range(10): 
    for x_val, y_val in zip(x_data, y_data): 
        grad = gradient(x_val, y_val) 
        w = w - lr * grad 
        print("\tgrad: ", x_val, y_val, round(grad, 4)) 
        l = loss(x_val, y_val) 
        
        
    print("progress:", epoch, "w=", round(w, 4), "loss=", round(l, 4)) 
    
# After training 
print("predict (after training)", "4 hours", forward(4))


"""

plt.plot(w_list, mse_list)
plt.ylabel('loss')
plt.xlabel('w')
plt.show()
"""