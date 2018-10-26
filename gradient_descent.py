#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:13:46 2018

@author: feebr01
"""

import numpy as np
import matplotlib.pyplot as plt


    
# simple implementation of gradient descent on a single function ###################################
x = np.arange(-3,4,1)

def func(x):
    y = x**2
    return y

y = [func(x) for x in x]


# derivative of function
def deriv_func(x):
    y = 2*x
    return y


# initialize values for optimization
x_vals = []
x=2
learn = .1
for i in range(1000):
    x = x - deriv_func(x)*learn
    x_vals.append(x)
plt.plot(x_vals)




# example of linear regression solved with gradient descent ########################################
# set up and plot points
x_points = [1,1,2,3,4,5,6,7,8,9,10,11]
y_points = [1,2,3,1,4,5,6,4,7,10,15,9]


# create y = mx + b formula inputs
m,b = 0,0

for i in range(500):
    y = lambda x : m*x + b 
    
    # learning rate (alpha)
    learn= .001
    
    # summation of error formulas
    theta_0 = sum(list(np.array(list(map(y, x_points))) - np.array(y_points)))
    theta_0_mean = theta_0 / len(x_points)*2   # multiply summation by 1/2m
    
     # same as theta_0, just scale all points by x_points by multiplying
    theta_1 = np.dot(np.array(theta_0),np.array(x_points))
    theta_1_mean = sum(theta_1) / len(x_points)*2 # multiply summation by 1/2m
    
    # apply summation formulas to learning formulas
    m = m - learn * theta_1_mean
    b = b - learn * theta_0_mean

# check final plot    
plt.scatter(x_points, y_points)
plt.plot(x_points, list(map(y, x_points)))








