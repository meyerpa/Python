# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:23:23 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:52 2017

@author: Paige
"""

from random import random,randrange
import numpy as np
import matplotlib.pylab as plt


def funct(x):
    value  = np.sin(x)**2 / (x*(1-x))
    return value


def prob_in(f, low, high, N):
    """Calculates average and deviation of a function f"""
    # Have random number of points    
    pts = np.random.uniform(low, high, size=(1, N))
    values  = f(pts)
    print("vals",values)
    # Divide by number of points and area to find probability
    prob = np.sum(np.abs(values)) / (N * (high-low))
    dev = np.sqrt(prob*(1-prob) / N)
    return prob, dev
    
    
N = 10000

prob, uncertainty = prob_in(funct, 0, 2, N)
print("prob within {:} +- {:.5f}".format(prob, uncertainty))