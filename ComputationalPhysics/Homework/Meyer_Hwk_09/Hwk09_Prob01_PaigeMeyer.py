# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:30:49 2017

@author: Paige Meyer
@date: 3/18/2017
@file: homework 09
@description: This file contains code to read sunspots.txt,
display the number of months, graph the sunspots with respect to time,
and average the data.
"""

import numpy as np
import matplotlib.pyplot as plt


def dft(y):
    """Returns the Fourier Transform of y.
    
    Parameters
    ----------
    y: numpy array
        The array values you want to transform
        
    Returns
    -------
    c: numpy array
        The Fourier Transformation of y.
    """
    N = len(y)
    n = np.arange(N)
    k = np.arange(N // 2 + 1)
    k = k[:, np.newaxis]                # add another dimension to k of size 1
    fourier_terms = y * np.exp(-2j * np.pi * k * n / N)
    c = fourier_terms.sum(axis=1)
    return c


r = 5

# read the data from sunspots.txt
data = np.loadtxt("sunspots.txt", float)
months = data[:, 0]
sunspots = data[:, 1]
# average sunpots period is approximately 3000/24 = 125 years
# since there are 24 peaks in 3000 months, also between every 500 
# year's there are approximately 4 peaks and troughs

print("A total of ", len(months), "months of sunspot data read in")

# plot sunspots, original file
plt.plot(months, sunspots, color="r", alpha=0.35, label="Sunspots")

# format plot
plt.xlabel("Month")
plt.ylabel("Number of sunspots")
plt.title("Sunspots over time")
plt.show()

# Discrete Fourier Transform Two Loops
df = 1 / (len(sunspots) * (months[1] - months[0])) 
fourier_transform = dft(sunspots)
plt.plot(df * range(len(fourier_transform)), np.abs(fourier_transform)**2)

# format plot
plt.title("Fourier Transform")
plt.xlabel("1/Period")
plt.ylabel("Amplitude")
plt.xlim(0, 0.02)
plt.title("Sunspots period")
plt.show()

# find the non-zero peak
fourier_transform = np.abs(fourier_transform)**2
maximum = np.argmax(fourier_transform[1:])
print("Fourier wave maximum", maximum)
period = 0
tol = 10e-15
for i in range(1, len(fourier_transform)):
    if maximum-fourier_transform[i] < tol:
        maximum = fourier_transform[i]
        period = df * i
print("period {:5f}".format(1/period))
# so I found the Fourier transform non-zero maximum 
# Using the maximum value, I found the cooresponding
# non-zero x-value maximum on the graph. Then, I took the inverse
# to find the period, which is approximately 130 days. This is similar to
# to my estimated 125 day period from part a.
