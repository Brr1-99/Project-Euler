"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import math
import itertools

def checkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

order = []
comb = itertools.permutations(range(1,8),7)

for x in comb:
    order.append(x)

prime = 0

for comb in order:
    num = int("".join(list(str(num) for num in comb)))
    if checkPrime(num) and num > prime:
        prime = num

print(f'The greatest n-digit pandigital prime is : {prime}')