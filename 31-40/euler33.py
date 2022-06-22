"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import math

fractions = []

for i in range(10,98):
    for j in range(i+1, 99):
        num_i = [i//10, i%10]
        num_j = [j//10, j%10]
        if num_i[0] in set(num_j):
            num_j.remove(num_i[0])
            if num_j[0] != 0:
                if i/j == num_i[1]/num_j[0]:
                    fractions.append([i,j])
        elif num_i[1] in set(num_j):
            if num_i[1] != 0:
                num_j.remove(num_i[1])
                if num_j[0] != 0:
                    if i/j == num_i[0]/num_j[0]:
                        fractions.append(i/j)

print(f'The value of the denominator for these four fractions is : {round(1/math.prod(fractions))}')