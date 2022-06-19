"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

order = []
comb = itertools.permutations(range(10),10)

for x in comb:
    order.append(x)

millionth = order[999999]

print(f'The millionth lexicographic permutation of the first 10 digits is : {millionth}')