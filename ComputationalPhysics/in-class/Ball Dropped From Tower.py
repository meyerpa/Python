from math import sqrt

h = float(input("Enter height of tower: "))
t = float(input("Please enter the seconds falling: "))
s = 9.81*t**2 / 2
if s < 0:
    s = h
print("The height at",h,"is", h-s, "meters")
time = sqrt(h *2/9.81)
print("The time it took to reach the ground is", time, "seconds")
