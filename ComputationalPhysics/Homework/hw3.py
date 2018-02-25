# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:30:49 2017

@author: Paige Meyer
@date: 1-26-2016
@file: homework3
@description: This file contains code to read sunspots.txt,
show the number of months, graph the sunspots with respect to time,
and average the data.
"""

import numpy as np
import matplotlib.pyplot as plt
from os.path import join

# format filename
filename = join("cpresources", "sunspots.txt")

# read the data from sunspots.txt
data = np.loadtxt(filename, float)
x = data[:, 0]
y = data[:, 1]

# take only first 1000 datapts
x = x[:1000]
y = y[:1000]

# calculate the average of ten points
avg = []
for i in x:
    summ = 0
    for j in np.linspace(i-5, i+5, 10):
        if j >= 0 and j < len(x):
            summ += y[int(j)]
    avg.append(1/(2*5)*summ)

# plot stuff
plt.plot(x, y, color="r", alpha=.3, label="Sunspot count")
plt.plot(x, avg, color="c", label="Average sunspots")
# format plot
plt.legend()
plt.xlabel("month")
plt.ylabel("number of sunspots")
plt.title("Sunspots vs. time")
plt.show()
