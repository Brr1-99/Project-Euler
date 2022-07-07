"""
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import math

def checkPrime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

notFound = True

i = 1

primes = [2]

while notFound:
    i += 2
    if checkPrime(i):
        primes.append(i)
    else:
        notFound = False
        for prime in primes:
            if math.sqrt((i-prime)/2) == int(math.sqrt((i-prime)/2)):
                notFound = True
                break

print(f'The smallest odd composite number tht cannot be written as the sum of a prime and twice a square is : {i}')