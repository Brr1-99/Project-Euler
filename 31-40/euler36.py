"""
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

suma = 0

def checkPalindrom(n):
    for i in range(int(len(n)/2)):
        if n[i] != n[-(1+i)]:
            return False
    return True

for i in range (1, 1000000, 2):
    if checkPalindrom(str(i)) and checkPalindrom(bin(i)[2:]):
        suma+= i

print(f'The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is : {suma}')