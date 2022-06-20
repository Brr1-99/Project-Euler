"""
n**2 + a*n + b
Find the product of the coefficients, a and b , for the quadratic expression that produces the maximum number of primes for consecutive values of n , starting with n = 0.
"""

import math

def checkPrime(n):
    for n in range(2, int(math.sqrt(n))+1):
        if n % n == 0:
            return False
    return True

max_primes = 0

i, j = 0,0

for a in range (-1000, 1001):
    for b in range(-1000, 1001):
        n=0
        while True:
            formula = n**2 + a*n + b
            if formula > 2 and checkPrime(formula):
                if n > max_primes:
                    max_primes = n
                    i, j = a, b
                n += 1
            else:
                break

print(i*j)