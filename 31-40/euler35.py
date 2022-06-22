"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math

def checkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

circular_primes = 13

for i in range(101, 1000000, 2):
    if checkPrime(i):
        circular_primes+=1
        letter = [num for num in str(i)]
        for i in range(len(str(i))):
            rotation = letter[i+1:] + letter[:i+1]
            num = int("".join(rotation))
            if not checkPrime(num):
                circular_primes -= 1
                break

print(f'There are {circular_primes} below one million.')