"""
17.6 Count of 2s
Write a method to count the number of 2s that appear in all the numbers between
0 and n (inclusive).
EXAMPLE
Input: 25
Output: 9 (2, 12, 20, 21, 22, 23, 24, and 25) Note that 22 counts for two 2s
"""

def countTwos(maximum):
    count = 0
    i = 0
    while 10**i < maximum:
        digit = (maximum % 10**(i+1))
        # add in additional numbers for this value
        if i != 0:
            count *= digit // 10**i
        # if digit is over 2, count all twos in digit
        if digit > 2:
            count += (2) * (10**i)
        elif digit == 2:
            count += digit % (10**(i))
        i += 1
    return count

print(countTwos(25))
