"""
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""

import itertools

order = []
comb = itertools.permutations(range(1,10),9)

for x in comb:
    order.append(x)

suma = 0
products = []

for c in order:
    prod1 = 10*c[0]+c[1]
    prod2 = 100*c[2]+10*c[3]+c[4]
    prod = 1000*c[5]+100*c[6]+10*c[7]+c[8]
    if prod1 * prod2 == prod and prod not in products:
        suma+= prod
        products.append(prod)

for d in order:
    prod1 = d[4]
    prod2 = 1000*d[0]+100*d[1]+10*d[2] + d[3]
    prod = 1000*d[5]+100*d[6]+10*d[7]+d[8]
    if prod1 * prod2 == prod and prod not in products:
        suma+= prod
        products.append(prod)

print(suma)