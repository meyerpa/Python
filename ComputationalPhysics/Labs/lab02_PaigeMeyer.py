# -*- coding: utf-8 -*-

"""
__author__="Paige Meyer"
__date__="01/11/2017"
__version__=1.0
PHYS 350 - Computational Physics
Lab 2
Description: This lab creates a random walk and graphs the walk.
"""

import numpy as np
import matplotlib.pyplot as plt
import randomwalker as walk

# Constants
step_size = .8          # size of each step
n_timesteps = 100       # number of steps in a walk
n_walk = 100            # number of random walks


# Create n_walk walks, plot distance, and find the sum
# of the distances
summ = np.zeros(n_timesteps)  # array for average distances
for i in range(n_walk):
    # create a random walk
    x_pos, y_pos = walk.make_walk(n_timesteps, step_size)

    dist = walk.mag(x_pos, y_pos)   # get distance
    plt.plot(dist, alpha=.2)        # plot distance for each walk

    summ += dist          # increment summ by current random walk distance

avg = summ/n_walk         # compute average distance
plt.plot(avg, color="k")  # plot average distance of walks
plt.title("Distance from Origin in walks")
plt.show()

print("Average distance from origin in all walks", avg[avg.size-1])

'''
Optional Part - As n_walks increases, the average distance varies less
    For example, when n_timesteps is 100 and n_walk = 10 can result
    in final average of 13.28, 15.04, 12.24, etc. While n_walk =100
    results in final averages of 13.13, 11.15, 12.81, 12.10, etc.
    Also, n_walk = 1000 resulted in observed final averages of
    12.39, 12.58, 12.59, etc. Thus, as n_walk increases the observed
    averages vary less.
Optional Part - What shape does the curve appear to take?
    The curve seems to take on a logarithmic curve.
    As n_timesteps increases, so does the average distance, but
    the relationship isn't linear. Instead, as n_timesteps increases,
    the final average also increases but not as much. It is similar
    to the economics problem of diminishing returns.
    Also, the function is (a bit) similar to doing the following
    >>> x = np.array(range(n_timesteps))
    >>> y = np.sqrt(np.log(x)*np.log(x))
    >>> plt.plot(x, y, color="m")

    After looking into the average of a random walk, I stumbled across
    Einstein's Brownian motion. The average seems to be a centered normal
    random variable. Although, I could not find which function the plot
    looks most like.

'''
