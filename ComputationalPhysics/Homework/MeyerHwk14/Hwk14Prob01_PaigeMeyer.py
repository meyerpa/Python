# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:52 2017

@author: Paige Meyer
Description: This program calculates the 
volume of a sphere and cylinder using Monte 
Carlo Techniques.
"""


import numpy as np
import matplotlib.pylab as plt


def v_sphere_cyl(N, hi=1, lo=-1, uncertainty=None):
    """Calculates volume of intersection of 3-D unit sphere
       and cyclinder
       
    parameters
    ----------
    N : integer
        Number of points
    hi : integer 
        the highest point to generate points
    lo : integer
        the lowest point to generate points
    uncertainty : float
        the uncertainty needed
    
    returns
    -------
    prob : float
        the probability of being within the area
    dev : float
        the deviation of the probabilty within the area
    
    """
    # Have random number of points    
    pts = np.random.uniform(lo, hi, size=(N, 3))
    # Find if each point falls within unit sphere
    n_in_sphere = np.sum(pts**2, axis=1) < 1
    # Find if each point falls within the the cyclinder
    n_in_cyl = ((pts[:, 0] - 0.5)**2  + pts[:, 1]**2) < 0.5
    # Find pts that fit both the cylinder and sphere
    n_tot = np.logical_and(n_in_cyl, n_in_sphere)
    # Divide by number of points to find probability
    prob = np.sum(n_tot)/N
    dev = np.sqrt(prob*(1-prob) / N)
    return prob, dev

    
stop = 6
dim = 3
probs = []
uncertainties = []
points =  np.logspace(4, 6, 10)

for N in points:
    prob, uncertainty = v_sphere_cyl(N)
    print("prob within {:} +- {:.5f} with {:.0f} points".format(prob, 
          uncertainty, N))
    
    probs.append(prob)
    uncertainties.append(uncertainty)

plt.errorbar(points, probs, yerr = uncertainties)
plt.title("Probability within 3-D unit circle and \
0.5 radius cylinder shifted 0.5")
plt.xscale('log')
plt.xlabel("Number of Points")
plt.ylabel("Probability")
plt.show()
