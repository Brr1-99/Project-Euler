"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

numbers = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 10,
    200: 10,
    300: 12,
    400: 11,
    500: 11,
    600: 10,
    700: 12,
    800: 12,
    900: 11,
    1000: 11,
    }

sum = 0

def less_hundred(n):
    global sum
    if n in numbers:
        sum+= numbers[n]
    else:
        sum+= numbers[10*(n//10)] + numbers[n%10]  

for i in range(1,100):
    less_hundred(i)

for i in range(100, 1001):
    if i in numbers:
        sum+= numbers[i]
    else:
        sum+= numbers[i//100] + 7  + 3
        less_hundred(i%100)

print(f'The number of letters used to spell the first 1000 numbers is : {sum}')