"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

import math

triang = lambda x: int(x*(x+1)/2)

def is_pent(x: int) -> bool:
	f = (0.5 + math.sqrt(0.25+6*x))/3
	if f - int(f) == 0:
		return True
	else:
		return False

def is_hex(x: int) -> bool:
	f = (1 + math.sqrt(1+8*x))/4
	if f - int(f) == 0:
		return True
	else:
		return False

i = 286

notFound = True

while notFound:
    tri = triang(i)
    if is_hex(tri) and is_pent(tri):
        notFound = False
        break
    i+= 1

print(f'The next triangle number that is also pentagonal and hexagonal is : {triang(i)}')