# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:52 2017

@author: Paige
"""

from random import random,randrange
import numpy as np
import matplotlib.pylab as plt


def v_sphere(n_dim, N):
    """Calculates volume of unit sphere of n_dim dimensions"""
    # Have random number of points    
    pts = np.random.uniform(-1, 1, size=(N, n_dim))
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
dims = np.arange(1, 10)
dim = 3
probs = []
uncertainties = []
point = 1e6
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


probs = []
uncertainties = []
for N in dims:
    prob, uncertainty = v_sphere(N, point)
    print("prob within {:} +- {:.5f}".format(prob, uncertainty))
    
    probs.append(prob)
    uncertainties.append(uncertainty)

plt.errorbar(dims, probs, yerr = uncertainties)
plt.title("Probability within unit circle")
plt.xlabel("Dimensions")
plt.ylabel("Probability")
plt.show()

"""
For three dimensions, the volume of the sphere is 4.19 and
the volume of the cube is 2^3 = 8. So the probability of a random
point falling within the sphere is 4.19/8 = 0.524, and this program
gives prob within 0.52 +- 0.04996, which is close to the actual 
value

As the dimensions increase, the uncertainty decreases.
This is due to the probability of all n points falling
within the circle decreases since there are much more 
points. In addition, the volume of the sphere decreases
with each dimension added.
"""
