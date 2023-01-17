from sympy.abc import a, b, s, t, u, v, w, x, y , z
from sympy import *

"""
All square roots are periodic when written as continued fractions and can be written in the form:

sqrt(n) = a0 + 1/(a1 + 1/(a2 + ...))

It can be seen that the sequence is repeating. For conciseness, we use the notation sqrt{23}=[4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
How many continued fractions N <= 10000 have an odd period?
"""

x, y = symbols('x y')

a = floor(sqrt(23))

fract = 7/(sqrt(23) - 3)

simply = simplify(fract)

num, den = together(simply).as_numer_denom()

integ = num.as_coeff_add()[0]

period = integ - den

print(period)