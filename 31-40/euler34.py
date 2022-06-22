"""
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""

import math

sumatorio = 0

for i in range(3, 1000001):
    num = str(i)
    suma = sum(math.factorial(int(n)) for n in num)
    if suma == i:
        sumatorio+= i
        
print(f'The sum of all numbers which are equal to the sum of the factorial of their digits is : {sumatorio}')