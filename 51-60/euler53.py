"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

How many, not necessarily distinct, values of  (n r) for 1 < n < 100 , are greater than one-million?
"""

import math

def comb(n: int, r: int) -> int:
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

greater = 0

for i in range (23, 101):
    for j in range(1,i):
        if comb(i,j) > 1000000:
            greater+= 1

print(f'There are {greater} values of  (n r) for 1 < n < 100 greater than one-million')