"""
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import math, itertools

primes = [2,3,5,7]

def checkPrime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(7,30000, 2):
    if checkPrime(i):
        primes.append(i)


notFound = True

while notFound:
        notFound = False
        for perm in list(itertools.permutations(primes, 5)):
            p = perm
            for i in range(0, 4):
                for j in range(i + 1, 5):
                    if not (checkPrime(int(str(i)+str(j))) and checkPrime(int(str(j)+str(i)))):
                        notFound = True
                        break

print(p)