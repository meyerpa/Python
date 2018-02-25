# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:52 2017

@author: Paige
"""


import numpy as np
import matplotlib.pylab as plt


def v_sphere(N, n_dim):
    """Calculates volume of intersection of 3-D unit sphere
       and cyclinder"""
    # Have random number of points    
    pts = np.random.uniform(-1, hi, size=(3, n_dim))
    # Find number that fall within unit sphere
    n_in_sphere = np.sum(pts**2, axis=1) < 1
    # Divide by number of points to find probability
    prob = np.sum(n_in_sphere)/N
    dev = np.sqrt(N*prob*(1-prob)) / N
    return prob, dev
    

def gen_point(low, high, n_dim, N):
    """Returns an array representing a between low and high of n_dim by N"""
    point = np.random.uniform(low, high, size=(N, n_dim))
    return point
    
stop = 6
dim = 3
probs = []
uncertainties = []
points =  np.logspace(1, stop, 10)

for N in points:
    prob, uncertainty = v_sphere(dim, N)
    print("prob within {:} +- {:.5f}".format(prob, uncertainty))
    
    probs.append(prob)
    uncertainties.append(uncertainty)

plt.errorbar(points, probs, yerr = uncertainties)
plt.title("Probability within {:} dimensional unit circle".format(dim))
plt.xscale('log')
plt.xlabel("Number of Points")
plt.ylabel("Probability")
plt.show()
