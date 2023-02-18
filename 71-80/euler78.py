"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

"""

def count_partitions(n, k=1, memo={}):
    """
    Counts the number of partitions of n as a sum of at least two positive integers, using k as the minimum value.
    """
    if n == 0:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    if k > n:
        return 0
    partitions = count_partitions(n-k, k, memo) + count_partitions(n, k+1, memo)
    memo[(n, k)] = partitions
    return partitions, memo

x, y = count_partitions(100, 1)

print(x,y)