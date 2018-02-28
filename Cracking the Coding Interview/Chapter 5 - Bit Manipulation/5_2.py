"""
Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR".
"""

def to_bin(x):
    # if the number cannot be represented n 32-bits, return ERROR
    if x % (2**(-32)) != 0.0:
        return "ERROR"
    # find the binary representation of x
    x_bin = ['.']
    x_curr = x
    i=1
    while x_curr != 0.0 and i <= 32:
        # check whether there is a 0 or 1 in this position
        if x_curr-2**(-i) >= 0:
            x_curr -= 2**(-i)
            x_bin.append('1')
        else:
            x_bin.append('0')
        i += 1
    return ''.join(x_bin)

print(to_bin(0.25))
print(to_bin(0.72))
