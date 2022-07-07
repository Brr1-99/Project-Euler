"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def gen_primes(lim: int) -> list[int]:
    primes = [x for x in range(lim)]
    for i in range(2, lim):
        if primes[i] != 0:
            for j in range(i, lim, +i):
                if i != j:
                    primes[j] = 0
    return list(filter(lambda p: (p != 0 and p != 1), primes))


lim = 10**6
primes = gen_primes(lim)
s = []

for i in range(len(primes)):

    a = primes[i]
    b = 1
    for j in range(i + 1, len(primes)):
        a += primes[j]
        b += 1
        if a > lim:
            break
        s.append([a, b])
m = (0, 0)

for i in s:
    if i[1] > m[1] and i[0] in primes:
        m = i

print(f'The prime which can be written as the sum of the most consecutive primes is {m[0]} with a total of {m[1]} consecutive primes')