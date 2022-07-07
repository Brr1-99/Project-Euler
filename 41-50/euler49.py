"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import math

def checkPrime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = []

for i in range(1491, 3340, 2):
    if checkPrime(i):
        primes.append(i)
        for j in range(1,3):
            if (not checkPrime(i+3330*j)) or set([num for num in str(i)]) != set([num for num in str(i+3330*j)]):
                primes.remove(i)
                break

print(f'The sequence is : {str(primes[0])+str(primes[0]+3330)+str(primes[0]+6660)}')