"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

It is interesting to note that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 

If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

import math

prime = 0

numbers = 1

i = 1

num = 1

def checkPrime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while prime/numbers > 0.1 or prime < 1:
    num+= 2*i
    if checkPrime(num):
                prime += 1
    for j in range(0,2):
        num += 2*i
        if checkPrime(num):
            prime += 1
    num+= 2*i
    numbers += 4
    i += 1

print(f'The length at which the ratio of primes falls below 10% is : {(i-1)*2 + 1}')