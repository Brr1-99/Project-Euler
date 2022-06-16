import math

"""
Find the sum of all the primes below two million.
"""

def checkPrime(x):
    prime = True
    for i in range(2, round(math.sqrt(x))+1):
        if x % i == 0:
            prime = False
            break
    return prime

sum = 2



for i in range(3, 2000000, 2):
    if checkPrime(i):
        sum += i


print(f'The sum of all the primes below two million is {sum}')