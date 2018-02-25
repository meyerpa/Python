"""
@author: Paige Meyer
Description: find illumination based on angle to light and show illumination
in a figure.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys


# Find intensity at each point
deg = 90
phi = deg * 2 * np.pi / 360                 # change angle to radians, because that's what np wants

# Define central difference here to approximate derivatives later on
def derivative_central(x, y):
    """Approximate first derivative using the central difference technique

    Parameters
    ----------
    x : numpy array
        The x-value of the function
    y : numpy array
        The y-values cooresponding to the x-values at the function

    Returns
    -------
    dy/dx : numpy array
        The approximation of the derivative in an N-2 dimensional
        numpy array

    """
    dy = y[1:]-y[:-1]
    dx = x[1:]-x[:-1]
    return dy / dx



## |---------------------------------------------------------------|
## |--------------------------WORLD MAP----------------------------|
## |---------------------------------------------------------------|

# Read in the altitudinal data, and denote where each point lies

# Read altitude.txt and save in variable called data
data = np.loadtxt("altitude.txt")
nrow, ncol = data.shape
stepsize = 30000

# Find x-positional values and y-positional
# Start at 0 and have steps of 30,000
x_pos = np.arange(0, ncol) * stepsize
y_pos = np.arange(0, nrow) * stepsize

# Plot the altitudinal data just read in to verify we have 
# the correct plot.

# Plot altitude
plt.figure(figsize=(48, 24))
plt.title("Altitude")
plt.imshow(data, vmin=-1000, vmax=1000, cmap="gray")
plt.colorbar()
plt.show()

# Find x slope
# Use central difference method to find slope in middle row points
# Since we are using the central difference, ensure first and last
# column and row are excluded, but these are ex
x_slope = np.ones([nrow-1, ncol-1])
for i in range(nrow-1):
    res = derivative_central(x_pos, data[i, :])
    x_slope[i, :] = res
    
# Find y-slope
# Use central difference method to find slope in middle column points
# Since we are using the central difference, ensure first and last
# column and row are excluded
y_slope = np.ones([nrow-1, ncol-1])
for j in range(ncol-1):
    res = derivative_central(y_pos, data[:, j])
    y_slope[:, j] = res

# calculate illumination
I = np.cos(phi) * x_slope + np.sin(phi) * y_slope     # calc. illumination
I = I / np.sqrt(x_slope**2 + y_slope**2 + 1)          # normalize illumination

# Plot the amount of light for the Earth.
plt.figure(figsize=(48, 24))
plt.title("Illumination")
plt.imshow(I, vmin=-0.1, vmax=0.1, cmap='gray')
plt.colorbar()
plt.show()


## |---------------------------------------------------------------|
## |------------------------------STM------------------------------|
## |---------------------------------------------------------------|

# Read in the scanning tunneling machine data
data = np.loadtxt("stm.txt")
nrow, ncol = data.shape                  
stepsize = 2.5                           # each point is 2.5 mm apart

# Find x-positional values and y-positional
# Start at 0, stepping by 2.5, stop when reach number of data points
x_pos = np.arange(0, ncol) * stepsize
y_pos = np.arange(0, nrow) * stepsize

# Plot STM
plt.figure(figsize=(48, 24))
plt.title("STM")
plt.imshow(data, cmap="gray")
plt.colorbar()
plt.show()


# Find x slope
# Use central difference method to find slope in middle row points
# Since we are using the central difference, ensure first and last
# column and row are excluded, but these are ex
x_slope = np.ones([nrow-1, ncol-1])
for i in range(nrow-1):
    res = derivative_central(x_pos, data[i, :])
    x_slope[i, :] = res
    
# Find y-slope
# Use central difference method to find slope in middle column points
# Since we are using the central difference, ensure first and last
# column and row are excluded
y_slope = np.ones([nrow-1, ncol-1])
for j in range(ncol-1):
    res = derivative_central(y_pos, data[:, j])
    y_slope[:, j] = res

# calculate illumination
I = np.cos(phi) * x_slope + np.sin(phi) * y_slope     # based on perpedicularity to light source
I = I / np.sqrt(x_slope**2 + y_slope**2 + 1)          # normalize I such that it varies from 0 to 1

# Plot result
plt.figure(figsize=(48, 24))
plt.title("Illumination")
plt.imshow(I, vmin=-0.4, vmax=0.4, cmap='gray')
plt.colorbar()
plt.show()
