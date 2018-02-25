# Excerise 2.2
from math import pi

# constants 
G = 6.67 * 10**(-11) # Newton's Graviational Constant
M = 5.97 * 10**24 # Mass of the Earth
R = 6371 # radius of Earth

T = float(input("Please enter the seconds for the satillite to orbit Earth: "))

# altitude above Earth's surface
h = ( (G*M*T**2) / (4*pi**2))**(1/3) - R
print("Altitude should be: ", h, "meters")
