# Composite Simpson's Rule
#from math import inf
def f(x):
    return 5 / (1 + x**4)

def frange(x, y, jump):
    tmplist = []
    while x <= y:
        tmplist.append(x)
        x += jump        
    return tmplist

##def fprime(x):
##    return -20*x**3 / (1 + x**4)**2
##
##def fprime2(x):
##    return -20*x**2 * (5*x**4 -3) / (1 + x**4)**3

def compSimp(data):
    h = (data[0]+data[-1]) / len(data)
    summ = f(data[0]) + f(data[-1])
    for i in range(len(data)-2):
        if i%2 == 0:
            summ += 4*f(data[i+1])
        else:
            summ += 2*f(data[i+1])
    return h/3 * summ

a = 0.0
b = 1.0
step = 1.0
epsilon = 10**-5
k = 100
compSimpLast = 10000000000.0
while True:
    data = frange(a, b, step)
    compSimpNew = compSimp(data)
    print("n = " + str(int(1/step)) + ": " + str(compSimpNew))
    if abs(compSimpLast - compSimpNew) < epsilon:
        print("Answer " + "{:.5f}".format(compSimpNew) + " with n = " + str(int(1/step)))
        break;
    else:
        step /= 2
        compSimpLast = compSimpNew
