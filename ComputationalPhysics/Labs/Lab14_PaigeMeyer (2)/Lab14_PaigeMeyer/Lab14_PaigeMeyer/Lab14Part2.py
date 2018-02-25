# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:23:23 2017

@author: Paige
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:52 2017

@author: Paige
Description: Uses the Mean Value Monte Carlo Method to
see what points lay under the curve denoted in funct.
"""

import numpy as np
import matplotlib.pylab as plt
import sys


def funct(x):
    """Function we are trying to integrate"""
    value  = np.sin(x)**2 / (x*(1-x))
    return value


def average(f, low, high, N):
    """Calculates average and deviation of a function f"""
    # Have random number of points    
    pts = np.random.uniform(low, high, size=(N, 1))
    values  = f(pts)
    # Divide by number of points and area to find probability
    avg = np.average(values)
    # f_var = np.sum(values**2) - np.average(values)**2
    dev = np.sqrt(N * np.var(values))
    return avg, dev
    
    
N = 1e8
N = int(N)
low = 0
high = 2

avg, uncertainty = average(funct, low, high, N)
I = np.abs(high-low) * np.abs(avg)
sigI = (np.abs(high-low) / N) * uncertainty
print("Area {:} +- {:.5f}".format(I, sigI))