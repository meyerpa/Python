# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:04:12 2017

@author: Paige Meyer
Description: Fourier transformation of an audiofile. It plots
both the original audiofile and the Fourier Transformation.
"""

import numpy as np
import pylab as plt
import time as time


def dft_two_loop(y):
    """Returns the Fourier Transform of y.
    
    Parameters
    ----------
    y: numpy array
        The array values you want to transform
        
    Returns
    -------
    c: numpy array
        The Fourier Transformation of y
    """
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n] * np.exp(-2j * np.pi * k * n / N)
    return c


def dft_one_loop(y):
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
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        fourier_terms = y * np.exp(-2j * np.pi * k * n / N)
        c[k] = np.sum(fourier_terms)
    return c
    

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


data = np.loadtxt("c4.txt",float)
times = data[:, 0]
y = data[:, 1]

plt.title("Original Audiofile")
plt.plot(times, y) # we use absolute value since they can be complex
plt.xlim(0, 0.05)
# note 13 from 0 to 0.05
plt.show()

# Discrete Fourier Transform Two loops
df = 1 / (len(y) * (times[1] - times[0]))        # assumes equal sample spacing

# Note: the plotting commands below throw an depreciation warning because the numpy arrays
# have a complex data type, but isn't technically an error, so I'm not going
# to cast them into real numbers to save computation time

# two loop function call
before = time.time()
two_loops = dft_two_loop(y)
two_loop_time = time.time() - before
plt.plot(df * range(len(two_loops)), np.abs(two_loops)**2, label="Two loops")

# one loop function call
before = time.time()
one_loop = dft_one_loop(y)
one_loop_time = time.time() - before
plt.plot(df * range(len(one_loop)), np.abs(one_loop)**2, label="One loop")

# no loop function call
before = time.time()
no_loop = dft(y)
no_loop_time = time.time() - before
plt.plot(df * range(len(no_loop)), np.abs(no_loop)**2, label="No loop")

# setting graph options
plt.title("Discrete Fourier Transform")
plt.xlim(0, 300)
plt.legend(loc=2)
plt.show()

# print time to complete each function call
# The one loop has major improvement over two loops,
# but depending on the run, the no loops may be faster or slower
# but the loops speed should be comperable. 
# Moreover, no loops is still faster than the two loops.
print("Two loops took {} seconds to complete".format(two_loop_time))
print("One loop took {} seconds to complete".format(one_loop_time))
print("No loop took {} seconds to complete".format(no_loop_time))
