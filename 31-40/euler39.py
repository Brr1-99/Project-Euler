"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math
C={}
for a in range(1,500):
	for b in range(a,500):
		c=int(math.sqrt(a*a+b*b))
		if a*a+b*b==c*c:
			try:
				C[a+b+c]+=1
			except KeyError:
				C[a+b+c]=1

mx=-1;
mxp=-1;
for (k, v) in C.items():
	if v>mx:
		mx=v
		mxp=k

print (f'The number of solutions is maximised for mxp = {mxp} with {mx} solutions.')