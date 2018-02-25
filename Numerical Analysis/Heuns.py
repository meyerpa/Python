'''Heun's Method'''
def frange(x, y, jump):
    tmplist = []
    while x <= y:
        tmplist.append(x)
        x += jump        
    return tmplist

def f(t, y):
    return -t * y + 4*t/y
    #return -y +t*(y**0.5)

def w(ti,wi, h):
    return wi + (h/4) * (f(ti,wi)+ 3* f(ti+(2/3)*h,wi + (2/3)*h*f(ti+(h/3),wi+h/3*f(ti,wi))))


a = 0.0
b = 1.0
h = 0.01
w0 = 1.0
for i in frange(a+h, b+h, h):
    #print(i)
    w0 = w(i-h, w0, h)
    
    print("t{:.3f}: {}".format(i,w0))
print("t{:.3f}: {}".format(b,w0))
from math import exp
def y(t):
    return (4 - 3*exp(-(t**2)))**.5
print("diff: " + str(y(1.0)-w0))
