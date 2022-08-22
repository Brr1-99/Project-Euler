"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. 

For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


"""
We just need to calculate the biggest number less than 1 mill than is divisible by every number, in order to have the fewer relatively prime.

This means multiply the consecutive prime numbers until we reach the limit.

2*3*5*7*11*13*17 = 510510 
"""

print('The value of n ≤ 1,000,000 for which n/φ(n) is a maximum is: 510510')