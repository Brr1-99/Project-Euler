"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

How many different ways can £2 be made using any number of coins?
"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = [0] * (200 + 1)
ways[0] = 1
for coin in coins:
    for j in range(coin, 200 + 1):
        ways[j] += ways[j - coin]

print(ways[200])