# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:30:49 2017

@author: Paige Meyer
@date: 1-26-2016
@file: homework 3
@description: This file contains code to read sunspots.txt,
display the number of months, graph the sunspots with respect to time,
and average the data.
"""

import numpy as np
import matplotlib.pyplot as plt

# format filename
filename = "sunspots.txt"
n_avg = 10

# read the data from sunspots.txt
data = np.loadtxt(filename, float)
# get the first 1000 data points
months = data[:1, 0]
sunspots = data[:1, 1]

# for each point, calculate the ten point average
avg_sunspots = []
for i in months:
    summ = 0
    # sum the values of the previous 5 and next 5 points
    for j in np.linspace(i-(n_avg/2), i+(n_avg/2), n_avg):
        # ensure not values outside sunspot data
        if j >= 0 and j < len(months):
            print(j)
            summ += sunspots[int(j)]
    # find average and append to the avg list
    avg_sunspots.append(1/(n_avg)*summ)

# plot stuff
plt.plot(months, sunspots, color="r", alpha=.35, label="Sunspots")
plt.plot(months, avg_sunspots, color="c", label="Average sunspots")
# format plot
plt.legend()
plt.xlabel("Month")
plt.ylabel("Number of sunspots")
plt.title("Sunspots vs. time")
plt.show()
