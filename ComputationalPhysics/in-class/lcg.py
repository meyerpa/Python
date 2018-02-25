import matplotlib.pyplot as plt

# Implement a linear congruent pseudorandom number generator

'''
DANGER: Changing the following constants may lead to undesired behaviour.
This particular set of a, c, and m is taken from Numerical Recipes.
The restrictions that exist on these constants for optimal behavour are
    1) m and c can't be co-divisible by any number other than 1.
    2) a-1 has to be divisive by all prime factors of m.
    3) a-1 has to be divisible by 4 is m is divisible by 4.
'''
a = 1664525
c = 1013904223
m = 4294967296

N = 1000      # Number of pseudorandom points to generate
x = 1         # Starting value
results = []  # initialize list (NOT an np.array) of results

for i in range(N):
    # Compute (ax + c) modulo m
    x = (a * x + c) % m
    results.append(x)

plt.plot(results, ".")
plt.xlabel("Trial")
plt.ylabel("Value")
plt.show()
