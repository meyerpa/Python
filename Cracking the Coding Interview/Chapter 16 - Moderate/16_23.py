"""
16.23 Rand 7 from Rand5
Implement a method rand7() given rand5(). That is, given a method that generates
a random number between 0 and 4 (inclusive), write a method that generates a
random number between 0 and 6 (inclusive).
"""

def rand7():

    while True:
        num = 5 * rand5() + rand5()
        if num < 21:
            return num % 7
