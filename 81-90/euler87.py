"""

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""

import itertools

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

# Fourth root of 50 mil is 84.x
power_4 = primes_less_than(84)

# Cube root of 50 mil is 368.x
power_3 = primes_less_than(368)

# Square root of 50 mil 7071.x
power_2 = primes_less_than(7071)

# Create all possible combinations from the three lists
numbers = list(itertools.product(*[power_2, power_3, power_4]))

# Obtain values which are less than 50 mil
diff = []
for number in numbers:
    value = number[0]**2 + number[1]**3 + number[2]**4 
    if value < 50000000:
        diff.append(value)

# Remove duplicate entries
unique_values = set(diff)

print(f"""There are {len(unique_values)} different numbers below 50 mil
      that can be expressed as p**2 + q**3 + r**4 where p,q,r are any prime numbers""")