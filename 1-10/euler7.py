"""
What is the 10 001st prime number?
"""

primes = [2]
number = 3
while len(primes) < 10001:
    primes.append(number)
    for prime in primes[:-1]:
        if number % prime == 0:
            primes.remove(number)
            break
    number+=2

print(f'The 10 001st prime number is {primes[-1]}')
