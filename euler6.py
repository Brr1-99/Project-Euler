"""
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
"""

summ = sum(i**2 for i in range (101))
squares = (100*101/2)**2
print(f'The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: {int(squares-summ)}')