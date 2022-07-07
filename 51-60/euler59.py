"""
Using a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words. 
Decrypt the message and find the sum of the ASCII values in the original text.
"""

with open("51-60/cipher.txt") as file:
    line = file.readline()
    numbers = line.split(',')
    
for number in numbers:
    print(number)