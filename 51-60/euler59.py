import itertools

"""
Using a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words. 
Decrypt the message and find the sum of the ASCII values in the original text.
"""

letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

combinations = list(itertools.product(letters, repeat=3))

common_words = [
    "the",
    "and",
    "is"
]

with open("51-60/cipher.txt", "r") as file:
    lines = file.readlines()
    words = []
    for line in lines:
        words += line.split(",")


for comb in combinations:
    text = ""
    for i in range(0, len(words)-1, 3):
        word = "".join([chr(ord(comb[0])^int(words[i])), chr(ord(comb[1])^int(words[i+1])), chr(ord(comb[2])^int(words[i+2]))])
        text += word

    has_common_words = True
    for word in common_words:
        if not(word + " " in text or " " + word in text):
            has_common_words = False
    if has_common_words:
        break

suma = 0

for word in text:
    for char in word:
        suma += ord(char) 

print(f"The sum of the decrypted message in ASCII is : {suma}")