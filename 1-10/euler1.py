"""
Problem 1:
Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples3 = int(1000/3)

multiples5 = int(1000/5) - 1

multiples15 = int(1000/15)

sum = multiples3*(multiples3+1)*3/2 + multiples5*(multiples5+1)*5/2 - multiples15*(multiples15+1)*15/2

print(f'The sum of all multiples of 3 or 5 below 1000 is: {int(sum)}')