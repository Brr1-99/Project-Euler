"""
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e .
"""

e = [2]
i = 1

while len(e) < 100:
    e.extend([1, 2*i, 1])
    i += 1


numerator = 1
denominator = e.pop()

# looping through the list to get the convergents
for i in e[::-1]:
    denominator, numerator =  (denominator * i + numerator, denominator)

print(f'The sum of the numerator is: {sum([int(digit) for digit in str(denominator)])}')