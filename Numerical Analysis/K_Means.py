#from __future__ import division
from random import random

# init means and data to random values
# use real data in your code
num_means = 10
num_values = 1000
means = [random() for i in range(num_means)]
data = [random() for i in range(num_values)]

param = 0.01 # bigger numbers make the means change faster
# must be between 0 and 1

for x in data:
    closest_k = 0;
    smallest_error = float("inf")
    for k in enumerate(means):
        error = abs(x-k[1])
        if error < smallest_error:
            smallest_error = error
            closest_k = k[0]
        means[closest_k] = means[closest_k]*(1-param) + x*(param)

# then plot each point, changing color based on mean part of
