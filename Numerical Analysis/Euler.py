# Euler Method
def yPrime(t, y):
    return -t * y + 4*t/y
    #return y - t**2 + 1

def w(prev_w, h, i, a):
    return prev_w + h*(yPrime(a+i*h, prev_w))

a = 0.0
b = 1.0
h = 0.01
wi = 1.0
for i in range(int((b-a)/h)):
    print("t{:.2f}: {}".format(a+i*h,wi))
    wi = w(wi, h, float(i),a)
print("t{}: {}".format(b,wi))
from math import exp
def y(t):
    return (4 - 3*exp(-(t**2)))**.5
print("diff: " + str(y(1.0)-wi))
