"""
8.1 Triple Step
A child is running up a staircase with n steps and can hop either 1, 2, or 3
steps at a time. Implement a method to count the number of ways a child
can run up the stairs.
"""

memo = dict()

def ctWays(n):
    """input
            n - number of stairs left (int)
        output
            ct - count of ways to run up with stairs remaining
    """
    if n == 0 :
        return 1
    elif n < 0:
        return 0
    else:
        # cache results, if not cached already
        if (n-1) not in memo:
            memo[n-1] = ctWays(n-1)
        if (n-2) not in memo:
            memo[n-2] = ctWays(n-2)
        if (n-3) not in memo:
            memo[n-3] = ctWays(n-3)

        # recurse to count ways taking 1, 2, and 3 stair step
        return memo[n-1] + memo[n-2] + memo[n-3]

print(ctWays(50))
