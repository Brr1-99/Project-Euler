"""
What is the value of the first triangle number to have over five hundred divisors?
"""

import math

def getDivisors(n: int)-> list[int]:
    divisors = [1]
    i = 1
    while i<= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n/i))
        i = i + 1
    return divisors

num_divisors = [1]

i = 1

while len(num_divisors) <= 500:
    new_div = getDivisors(sum(range(i+1)))
    if new_div > num_divisors:
        num_divisors = new_div
    i+= 1

print(f'The first triangle number with over 500 divisors is "{sum(range(i))}" with a total of "{len(num_divisors)}"')