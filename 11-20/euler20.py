"""
Find the sum of the digits in the number 100!
"""
import math

sum = 0

for n in str(math.factorial(100)):
    sum+= int(n)

print(f'The sum of the digits of 100! is: {sum}')