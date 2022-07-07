"""
Evaluate the sum of all the amicable numbers under 10000.
"""

import math

amicable = 0

def getDivisorsSum(n: int) -> list[int]:
    divisors = []
    i = 1
    while i<= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n/i))
        i = i + 1
    if len(divisors) > 1:
        divisors.remove(n)

    return sum(divisors) 

for j in range(1,10000):
    a = getDivisorsSum(j)
    if j == getDivisorsSum(a) and a!= j:
        amicable+= j + a

print(f'The sum of the amicable numbers lower than 10000 is : {int(amicable/2)}')