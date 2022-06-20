"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

numbers = []

for i in range (1000, 1000000):
    number = str(i)
    suma = sum(int(n)**5 for n in number)
    if suma == i:
        numbers.append(i)

print(f'The sum of all numbers that can be written as the sum of fifth powers of their digits is : {sum(numbers)}')