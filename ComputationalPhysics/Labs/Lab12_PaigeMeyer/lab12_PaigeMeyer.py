# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:25:38 2017

@author: Paige Meyer
@lab: 12
Description: Solves Laplace's Equation and Poisson's Equation
  using the Relaxation Method
"""

import numpy as np
import matplotlib.pylab as plt


def rho(i, j):
    """Fuction checks if i and j are within ranges within charge distro.
    
    parameters
    ----------
    i : float
        position for x-axis left being 0
    j : float
        position for y-axis top being 0
        
    returns
    -------
    charge : int
        1 if has positive charge, -1 is negative charge, and 0 if no charge.
    """
    if i > b and i < (b+C):
        if j > b and j < (b+C):
            return 1
    if i > (L-b-C) and i < (L-b):
        if j > (L-b-C) and j < (L-b):
            return -1
    return 0


# constants
N = 18              # number points for each column and row
L = 1               # 1 meter long
tol = 8.854e-12     # tolerance for charge
delta = tol * 4     # tolerance for array
a = 1               # charge
dxy = L/N           # step size
b = 0.1             # offset for charge block
C = .5              # charge block length/height

# arrays
phi = np.zeros([N+1, N+1])
phi[0, :] = 10              # top of plate is 10
phi[-1, :] = -10            # the bottom of the plate is -10
phiNew = np.copy(phi)
rhoarray = np.copy(phi)


# find charge distro.
for i in range(N+1):
    for j in range(N+1):
        rhoarray[i, j] = rho(i*dxy, j*dxy)

# update values in array until get new ones using Poisson's equation
while delta > tol:
    # use 4 surrounding potentials to updated the current potential, plus  
    # the charge at the current position
    phiNew = (1/4) * (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) + \
                      np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) + \
                      a**2 * rhoarray / tol)
    
    # reset top and bottoms to keep charge
    phiNew[:, 0] = phi[:, 0]
    phiNew[:, -1] = phi[:, -1]
    phiNew[0, :] = phi[0, :]
    phiNew[-1, :] = phi[-1, :]

    # get practical error between new phi and old phi
    delta = np.max(phiNew - phi)
    # update phi to be phiNew
    phi, phiNew = phiNew, phi


# plot result  with contour map
# get positions
x = np.linspace(0, L, N+1)
y = np.linspace(0, L, N+1)
x, y = np.meshgrid(x, y)

# adjust levels and color
levels = np.linspace(phi.min(), phi.max(), 20)
cmap = plt.get_cmap('gist_earth')

# plot
plt.contourf(x[:-1, :-1]+dxy/2., y[:-1, :-1]+dxy/2., 
             phi[:-1, :-1], levels=levels, cmap=cmap)
plt.colorbar()
# add labels
plt.title("Charge distribution")
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.show()
