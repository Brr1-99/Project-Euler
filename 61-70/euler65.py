"""
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e .
"""

from math import factorial
from fractions import Fraction

e = 0

for i in range(0,150):
    e+= 1/factorial(i)

numerator = str(Fraction(e).limit_denominator()).split('/')[0]

print(sum(int(n) for n in numerator))