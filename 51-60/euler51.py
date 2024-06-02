"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [x for x in range(n+1) if primes[x] and x > 100000]

def check_filter(x: int):
    data = {c: str(x).count(c) for c in set([m for m in str(x)])}
    keys = [key for key, val in data.items() if val >= 3]
    if keys != []:
        return True, str(x).replace(str(keys[0]), '*')
    else:
        return False, '0'

primes = sieve_of_eratosthenes(1000000)

filtered_primes = []
for x in primes:
    is_filtered, new_p = check_filter(x)
    if is_filtered:
        filtered_primes.append(new_p)

filtered_set = {c: filtered_primes.count(c) for c in set(filtered_primes)}
keys = [key for key, val in filtered_set.items() if val >= 6]

print(keys) # ['*7*9*7', '2***03', '37***3', '**7*67', '9*8**3', '***109', '8**8*1', '4*3**3', '*2*3*3', '*6*0*7']

# Remove ***109 because no posible 3 digit prime
# Then smallest after checking all families have 8 primes