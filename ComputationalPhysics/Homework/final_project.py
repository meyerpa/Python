"""
@author: Paige Meyer
Description: find illumination based on angle to light
"""

import numpy as np
import matplotlib.pyplot as plt


# Find intensity at each point
phi = 185                                   # angle of light in degrees
phi = phi * 2 * np.pi / 360                 # change angle to radians, because that's what np wants

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



# Read altitude.txt and save in variable called data
data = np.loadtxt("altitude.txt")
nrow, ncol = data.shape
stepsize = 30000

# Find x-positional values and y-positional
# Start at 0 and have steps of 30,000
x_pos = np.arange(0, ncol) * stepsize
y_pos = np.arange(0, nrow) * stepsize

# Plot altitude
plt.figure(figsize=(12, 6))
plt.title("Altitude")
plt.imshow(data, vmin=-1000, vmax=1000, cmap="gray")
plt.colorbar()
plt.show()

# Find x and y slope
# Use central difference method to find slope in middle row points

# NOTE: GET RID OF LOOP
x_slope = np.empty([nrow-1, ncol-1])
for i in range(nrow-1):
    res = derivative_central(x_pos, data[i, :])
    x_slope[i, :] = res
    
# Find y-slope
# Use central difference method to find slope in middle row points
# NOTE: GET RID OF LOOP
y_slope = np.empty([nrow-1, ncol-1])
for j in range(ncol-1):
    res = derivative_central(y_pos, data[:, j])
    y_slope[:, j] = res

# calculate illumination
I = np.cos(phi) * x_slope + np.sin(phi) * y_slope     # based on perpedicularity to light source
I = I / np.sqrt(x_slope**2 + y_slope**2 + 1)          # normalize I such that it varies from 0 to 1

# Plot result
plt.figure(figsize=(12, 6))
plt.title("Illumination")
plt.imshow(I, vmin=-0.1, vmax=0.1, cmap='gray')
plt.colorbar()
plt.savefig("I{:}.png".format(phi))
plt.show()


## |---------------------|
## |---------STM---------|
## |---------------------|

# Read in the scanning tunneling machine data
data = np.loadtxt("stm.txt")
nrow, ncol = data.shape                  
stepsize = 2.5                           # each point is 2.5 mm apart

# Find x-positional values and y-positional
# Start at 0, stepping by 2.5, stop when reach number of data points
x_pos = np.arange(0, ncol) * stepsize
y_pos = np.arange(0, nrow) * stepsize

# Find x-slope
# Use central difference method to find slope in middle row points
x_slope = np.empty([nrow-1, ncol-1])
for i in range(nrow-1):
    res = derivative_central(x_pos, data[i, :])
    x_slope[i, :] = res
    
# Find x-slope
# Use central difference method to find slope in middle row points
y_slope = np.empty([nrow-1, ncol-1])
for j in range(ncol-1):
    res = derivative_central(y_pos, data[:, j])
    y_slope[:, j] = res
    
# calculate illumination
I = np.cos(phi) * x_slope + np.sin(phi) * y_slope     # based on perpedicularity to light source
I = I / np.sqrt(x_slope**2 + y_slope**2 + 1)          # normalize I such that it varies from 0 to 1

# Plot result
plt.figure(figsize=(12, 6))
plt.title("Illumination")
plt.imshow(I, vmin=-0.4, vmax=0.4, cmap='gray')
plt.colorbar()
plt.savefig("I{:}.png".format(phi))
plt.show()
