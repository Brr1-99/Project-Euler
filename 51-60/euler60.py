"""
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [x for x in range(n+1) if primes[x]]

def checkPrime(x: int) -> bool:
    prime = True
    for i in range(2, round(math.sqrt(x))+1):
        if x % i == 0:
            prime = False
            break
    return prime

def find_lowest_prime_sum(n):
    def is_prime(x):
        return checkPrime(x)

    def check_concatenation(p1, p2):
        return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))

    primes = sieve_of_eratosthenes(1000000)
    prime_list = []
    for prime in primes:
        prime_list.append(prime)
    result = []
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            if check_concatenation(prime_list[i], prime_list[j]):
                result.append((prime_list[i], prime_list[j]))

    primes = []
    for prime1, prime2 in result:
        if prime1 not in primes:
            primes.append(prime1)
        if prime2 not in primes:
            primes.append(prime2)
        if len(primes) == n:
            break

    return sum(primes),primes

print(find_lowest_prime_sum(5))