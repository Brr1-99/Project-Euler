"""
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
"""

import math

def checkPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

sum = 0 

i = 11

find = 0

while find < 11:
    if checkPrime(i):
        letter = [num for num in str(i)]
        find += 1
        sum+= i
        for j in range(len(str(i))-1):
            delete_left = letter[j+1:]
            num_left = int("".join(delete_left))
            delete_right = letter[:-(j+1)]
            num_right = int("".join(delete_right))
            if not checkPrime(num_left) or not checkPrime(num_right):
                find -= 1
                sum -= i
                break
    i+=2

print(f'The sum of the only eleven primes that are both truncatable from left to right and right to left is : {sum}.')