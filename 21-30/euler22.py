"""
What is the total of all the name scores in the file?
"""

with open("21-30/names.txt") as file:
    names = []
    for line in file:
        for name in line.split(','):
            names.append(str(name[1:-1]))

ordered = sorted(names)

score = 0

# Ord contiene el valor para el código Unicode : a-> 97 , b-> 98 ...
# El inverso de la función ord() es chr()
# Se puede hacer tanto para mayúsculas como minúsculas

for idx, name in enumerate(ordered):
    individualScore = 0
    for letter in name:
        individualScore += ord(letter) - 64
    score+= (idx+1)* individualScore

print(f'The total score for all names in the file is : {score} ')