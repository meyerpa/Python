"""
10.8 Find Duplicates
You have an array with all the numbers from 1 to N, where N is at most 32,000.
The array may have duplicate entries and you do not know what N is. With only
4 kB of memory available, how would you print all duplicate elements in the
array?
"""

bitlist = []
for i in range(32000):
    bitlist.append(False)

def printDuplicates(a):
    """Prints all the duplicates in a (highest int is 32,000)"""
    for num in a:
        if bitlist[num - 1]:
            bitlist[num - 1] = True
        else:
            print(num)
