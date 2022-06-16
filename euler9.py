"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def check_pathagorean(a, b, c):
    return a**2 + b**2 == c**2

for a in range(1, 332):
    for b in range(a+1, int(((1000-a)/2 -1))):
        c = 1000 - a - b
        if (check_pathagorean(a, b, c)):
            print (f'The triplet is: {a}, {b}, {c} and its product is {a*b*c}')
            break