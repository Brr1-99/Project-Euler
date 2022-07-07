"""
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

notFound = True

i = 645

def factorize(n: int) -> list[int]:
    factors = []
    while (n & 1) == 0:
        factors.append(2)
        n >>= 1
    for d in range(3, 1 << 60, 2):
        if d * d > n:
            break
        while n % d == 0:
            factors.append(d)
            n //= d
    if n > 1:
        factors.append(n)
    return factors

while notFound:
    i+= 1
    unico = []
    for j in range(i, i+4):
        factorJ = factorize(j)
        if len(set(factorJ)) == 4:
            for factor in set(factorJ):
                unico.append(factor**factorJ.count(factor))
    if len(set(unico)) == 16:
        notFound = False


print(f'The first of the four consecutive integers to have four distinct prime factors each is : {i}')