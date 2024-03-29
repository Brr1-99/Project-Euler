"""
How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100?
"""

import itertools

pairs = []
comb = itertools.combinations_with_replacement(range(2,101),2)

for x in comb:
    pairs.append(x)

products = []

for pair in pairs:
    products.append(pair[0]**pair[1])
    products.append(pair[1]**pair[0])


l = []
for a in range(2,101):
        for b in range (2,101):
                c = a**b
                if c not in l:
                        l.append(c)
print (len(l))

print(f'There are {len(set(products))} distinct terms in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100')