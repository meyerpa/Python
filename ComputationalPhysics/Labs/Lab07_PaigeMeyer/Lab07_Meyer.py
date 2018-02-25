# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:05:29 2017

@author: Paige Meyer
@date="02/22/2017"
@version= 1.1
PHYS 350 - Computational Physics
Lab 07
Description: Shows Time evolution of Qunatum Systems with Eigenvalues
and Eigenfunctions

"""

import numpy as np
from numpy.linalg import eigh
import matplotlib.pyplot as plt


def Normalize(x):
    """Returns the normalized x vector

    Parameters
    ----------
    s : numpy array
        Holds each point in the vector

    Returns
    -------
    s : numpy array
        Holds each normalized point in the vector, total length is one
    """
    return x / np.sqrt(np.dot(np.conjugate(x), x))


def Psi(valH, vectH, PsiInitial, t):
    """Return the wave funcction at a certain time t

    Parameters
    ----------
    valH : numpy array
        Array of eigenvalues
    vectH : numpy array
        Array of eigenvectors
    PsiInitial : numpy array
        Normalized initial wavefunction
    t : float, optional
        time to evaluate the wavefunction

    Returns
    -------
    PsiFinal : float
        Energy at any time t for this system
    """
    PsiValue0 = np.dot(np.conjugate(vectH[:,0]), PsiInitial) * np.exp(-1j * valH[0] * t) * vectH[:,0]
    PsiValue1 = np.dot(np.conjugate(vectH[:,1]), PsiInitial) * np.exp(-1j * valH[1] * t) * vectH[:,1]
    return PsiValue0 + PsiValue1
    
time = 100                 # number of times to loop
x = np.array([1, 1j], dtype=complex)
x = Normalize(x)

psiInit = np.array([1, 0], dtype=complex)      # Initial molecule state
# Hamiltonian Matrix (determines molecular states change with time)
H = np.array([[1, 1],
              [1, 1]])  

vals, vect = eigh(H)
#print(vals, vect)

times = np.linspace(0, 10, time+1)
probs = np.empty(time+1, dtype=complex)

i = 0
for i in range(time+1):
    # get PsiValue at each time
    psiValue = Psi(vals, vect, psiInit, times[i])
    # calculate probability
    prob = np.abs(np.dot(np.conjugate(psiValue), psiInit)) ** 2
    # updated probability in array
    probs[i] = prob
    

# format plot
plt.plot(times, probs, color="b", label="State [0,1]")

# To ensure if the initial state is an eigenvector the probability for that
# measurement at any time t is one, I made PsiInitial one of the eigenvectors
# ([0.70710678, 0.70710678]) and checked that the probability was 1.
# Regarding ensuring that starting in one eigenstate, there is a 0% change of being
# in the other eigenstate, 
# I made line 72 --prob = np.abs(np.dot(np.conjugate(psiValue), psiInit)) ** 2
# to have np.array([-0.70710678, 0.70710678]), and ensured that the probabilty was 
# zero for the other state

# optional 
for i in range(time+1):
    # get PsiValue at each time
    psiValue = Psi(vals, vect, psiInit, times[i])
    # calculate probability
    prob = np.abs(np.dot(np.conjugate(psiValue), np.array([0,1]))) ** 2
    # updated probability in array
    probs[i] = prob

# format plot
plt.plot(times, probs, color="r", label="State [1,0]")
plt.legend()
plt.title("Probability vs. Time")
plt.xlabel("Time")
plt.ylabel("Probability")
plt.show()