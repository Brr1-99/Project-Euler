"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

with open("41-50/words.txt") as file:
    words = []
    for line in file:
        for word in line.split(','):
            words.append(str(word[1:-1]))

triangular_numbers = []

for i in range(25):
    triangular_numbers.append(0.5*i*(i+1))

triangle = 0

for word in words:
    individualScore = 0
    for letter in word:
        individualScore += ord(letter) - 64
    if individualScore in triangular_numbers:
        triangle += 1

print(f'There are {triangle} triangle words in the text file.')