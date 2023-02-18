"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

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
    return partitions

num_partitions = count_partitions(100, 1)
print(num_partitions)