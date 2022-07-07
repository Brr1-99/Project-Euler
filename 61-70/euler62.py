"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from itertools import count

cubes = {} 

def find(n: int) -> int:
    for i in count(start=345):
        key = ''.join(sorted(str(i*i*i)))
        if key in cubes:
            value = cubes[key]
            value[0] += 1
            if value[0] >= n:
                return value[1]**3
        else:
            cubes[key] = [1, i]

print(f'The smallest cube for which exactly five permutations of its digits are cube is: {find(5)}')