"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math

def getDivisorsSum(n):
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

abundant = []

sums = [False]*28124

total = 0

for i in range(1, 28124):
    if getDivisorsSum(i) > i:
        abundant.append(i)

for i in range(0, len(abundant)-1):
    for j in range(0, len(abundant)-1):
        if abundant[i] + abundant[j] <= 28123:
            sums[abundant[i] + abundant[j]] = True
        else:
            break

for i in range(1, 28124):
    if not sums[i]:
        total+= i

print(total)