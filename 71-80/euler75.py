"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

"""

from tqdm import tqdm
import itertools
import math

numbers = itertools.combinations(range(3, 100001),2)

def calculate_third_side(x: int, y: int) -> float:
    return math.sqrt(x**2 + y**2)

found = []

for x,y in tqdm(numbers, ncols = 100):

    z = calculate_third_side(3,4)

    if z.is_integer() and x+y+z <= 1500000:
        found.append(x+y+z)

print(len(found))