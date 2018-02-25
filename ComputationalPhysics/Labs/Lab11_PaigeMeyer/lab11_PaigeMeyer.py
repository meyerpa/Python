# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:35:49 2017

@author: Paige Meyer

Code for finding energy values of a particle in a box (aka Finite Well).
This code will solve for the  
"""

import numpy as np
import matplotlib.pyplot as plt


def V(x, L=1.0):
    '''Returns potential energy function in units of eV with a given width
    (in nm)
    
    parameters
    ----------
    x : float
        position
    width : float
        width of the potential well. Default is 1.0, optional.
    '''
    if x > 0 or x < L:
        return 0
    else: 
        return 1000


def func(Psi, x, V=V, E=5, m=1, hbar=1):
    # Returns the derivative. This is 
    d2Psi_dx2 = -(2*m / hbar**2) * (E - V(x))*Psi[0]
    return np.array([Psi[1], d2Psi_dx2])


def diff(E, psi0 = 0.0, d_psi=0.0, x=np.array([0])):
    """Retuns the difference in Energy at the boundary condition 
    
    Note: times should define an array of times called times,
    and a function that gives the derivative called func.  
    """
    psi_init = [psi0, d_psi]
    psi = rk4(func, psi_init, pos, E=E)
    return psi[-1, 0]


def secant_solver(f, x0, x1, tol=1e-15, n_max=100, n=1, **kwargs):
    """Finds root (0) of function with initial energy around x0 and x1
    """
    f0 = f(x0, **kwargs)
    f1 = f(x1, **kwargs)
    # ensure will not have divide by zero error
    if np.abs(f1-f0) < tol:
        delta = np.abs(x1 - x0)             # difference
        print("Returning early", np.abs(f1-f0))
        return (n, x1, delta)
    
    # compute new x
    x = x1 - f1*(x1 - x0) / (f1 - f0)
    delta = np.abs(x - x1)                  # difference
    
    # if new x is within tolerence, return otherwise do again
    if delta < tol or n > n_max:
        return (n, x, delta)
    else:
        return secant_solver(f, x1, x, tol, n_max, n+1, **kwargs)

    
def rk4(f, x0, t, **kwargs):
    # Pass in the function for dx/dt, the initial value, x0, and an array
    # of times and return an array of x values for those times.
    x = x0        # track the current value of x
    xlist = x  # Create an array of x values at all times
    lasttime = t[0]

    for time in t[1:]:
        # This loop needs to compute h based on time and lasttime
        # (since it isn't automatically "known" to the euler function)
        h = time - lasttime
        k1 = h * f(x, lasttime, **kwargs)
        k2 = h * f(x + (k1/2), lasttime + (h/2), **kwargs)
        k3 = h * f(x + (k2/2), lasttime + (h/2), **kwargs)
        k4 = h * f(x + k3, lasttime + h, **kwargs)
        x = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        # Add x to the xlist array.  To do this, we have to over-write the
        # xlist array using vstack (which stacks the arrays in 'rows' or
        # vertical stacks).  Since x is a scalar, we have to
        # convert it into an array first, and then 'stack' it.
        xlist = np.vstack((xlist, x))

        # Update the lasttime variable so it is ready for the next loop.
        lasttime = time

    return xlist

# Set up limits and step number
Psia = 0.0           # wave function at end of first wall
Psib = 0.0           # wave function at end of first wall
m = 1                # mass
hbar = 1             # h_bar
E = 5
a = 0.0              # start position
b = 1.0              # end position
N = 10000            # steps

pos = np.linspace(a, b, N)


# potential energy
vfunc = np.vectorize(V)
potential = vfunc(pos)

# Find first energy level answer using secant solver
(n, energy, epsilon) = secant_solver(diff, E-1, E, tol=1e-4, n_max=20,
    psi0=0, d_psi=0.1, x=pos)
print("Used Secant solver {:} times to find initial energy {:.5f}\
 with error {:.5f}".format(n, energy, epsilon))

# initial conditions
psi0 = np.array([Psia, 0.1])    # x(a) = initial energy, initial derivative.
rk1 = rk4(func, psi0, pos, E=energy)

# print final energy
print("Final energy", rk1[-1, 0])


# Find first energy level answer using secant solver
(n, energy, epsilon) = secant_solver(diff, 11, 13, tol=1e-4, n_max=20,
                             psi0=0, d_psi=0.1, x=pos)
print("Used Secant solver {:} times to find initial energy {:.5f}\
 with error {:.5f}".format(n, energy, epsilon))

# initial conditions
rk2 = rk4(func, psi0, pos, E=energy)

# Find first energy level answer using secant solver
(n, energy, epsilon) = secant_solver(diff, 30, 35, tol=1e-4, n_max=20,
                             psi0=0, d_psi=0.1, x=pos)
print("Used Secant solver {:} times to find initial energy {:.5f}\
 with error {:.5f}".format(n, energy, epsilon))

# initial conditions
rk3 = rk4(func, psi0, pos, E=energy)


# plotting commands
plt.plot(pos, potential, label="Potential Energy")
plt.plot(pos, rk1[:, 0], label="Wave n=1")
plt.plot(pos, rk2[:, 0], label="Wave n=2")
plt.plot(pos, rk3[:, 0], label="Wave n=3")
plt.title("Energy in Finite Well")
plt.ylabel("$\\psi(x)$")
plt.xlabel("position (meters)")
plt.legend()
plt.show()
