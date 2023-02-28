"""

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""

def primes_less_than(n):
    """
    Returns a list of prime numbers less than n.
    """
    # create a boolean array of size n, initially set to True
    is_prime = [True] * n
    
    # set the first two numbers (0 and 1) to False, since they are not prime
    is_prime[0] = is_prime[1] = False
    
    # use the Sieve of Eratosthenes algorithm to mark all multiples of prime numbers as not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False
    
    # return a list of prime numbers less than n
    return [i for i in range(n) if is_prime[i]]

power_4 = primes_less_than(84)

power_3 = primes_less_than(368)

power_2 = primes_less_than(7071)