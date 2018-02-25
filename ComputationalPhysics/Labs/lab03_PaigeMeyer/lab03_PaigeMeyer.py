# -*- coding: utf-8 -*-

"""
__author__="Paige Meyer"
__date__="01/25/2017"
__version__= 1.2
PHYS 350 - Computational Physics
Lab 3
Description: This lab creates some random walks, graphs the walks,
averages the walks, and shows the standard deviation for the walks.
"""

import numpy as np
import matplotlib.pyplot as plt
import randomwalker_PaigeMeyer as walk
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Constants
step_size = 1           # size of each step
n_timesteps = 10      # number of steps in a walk
n_walk = 10            # number of random walks


walks = np.empty([n_timesteps, 3, n_walk])
# Create n_walk walks, plot distance, and find the sum
# of the distances
all_walk_dist = np.zeros([n_timesteps, n_walk])  # all walk distances
summ = np.zeros(n_timesteps)
for i in range(n_walk):
    # create a random walk
    values = walk.make_walk(n_timesteps, step_size)
    dist = walk.mag(values)         # get distance
    summ += dist                    # increment distance sum
    walks[:, :, i] = values         # add current walk ot list of walks

    all_walk_dist[:, i] = dist      # add new distance to all walk distance
    plt.plot(dist, alpha=.2, color="cyan")  # plot walk distance

avg = summ/n_walk         # compute average distance

sumofsq = np.zeros(n_timesteps)
for i in range(n_walk):
    sumofsq += ((all_walk_dist[:, i] - avg)**2)

std_dev = np.sqrt(1/(n_walk - 1) * sumofsq)  # standard deviation for all walks

# plot average and standard deviations for walks
plt.plot(avg, color="k", label="average walk")
plt.plot(avg+std_dev, color="r", label="standard deviation")
plt.plot(avg-std_dev, color="r")  # plot average walk lower deviation
plt.title("Walks' Distance from Origin")
plt.legend()
plt.savefig("Walks' Distance from Origin.png")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(n_walk):
    ax.plot(walks[:, 0, i], walks[:, 1, i], walks[:, 2, i], '-r', color='cyan')
ax.set_xlabel('x position')
ax.set_ylabel('y position')
ax.set_zlabel('z position')
ax.set_title(str(n_walk) + " Three-dimensional Random Walks")

print("Average distance at end of all walks", avg[-1])
