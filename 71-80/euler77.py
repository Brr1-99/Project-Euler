"""
It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

import itertools
from sympy import isprime

def prime_combinations(n):
    primes = [x for x in range(2, n) if isprime(x)]
    for i in range(1, len(primes)):
        for comb in itertools.combinations(primes, i):
            if sum(comb) == n:
                yield comb

print(len(list(prime_combinations(10))))