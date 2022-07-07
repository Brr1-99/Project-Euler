"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

"""
The base of the power must be a number less than 10. That is because 10**n produces n+1 digits: a single one and n zeros.
"""

found = True

nums = 0

i = 1

while found:
    found = False
    for j in range(1, 10):
        if len(str(j**i)) == i:
            nums += 1
            found = True
    i += 1

print(f'There are {nums} n-digit positive integers which are an nth power.')