"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. 
You are given that for every number below ten-thousand, it will either become a palindrome in less than fifty iterations, or no one, has managed so far to map it to a palindrome.

How many Lychrel numbers are there below ten-thousand?
"""

def palindrome(n: int) -> tuple[int, bool]:
    suma = n + int(str(n)[::-1])
    return suma, str(suma)==str(suma)[::-1]

lychrel = 0

for i in range(10001):
    lychrel += 1
    j = 0 
    number = i
    while j < 50:
        number, palind = palindrome(number)
        if palind :
            lychrel -= 1
            break
        j += 1

print(f'There are {lychrel} numbers below ten-thousand')