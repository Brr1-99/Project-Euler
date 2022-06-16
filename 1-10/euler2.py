"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

a, b = 0, 1

sum = 0

while True:
    a, b = b, a+b
    if b >= 4000000:
        break
    if b % 2 == 0:
        sum+= b
        
print(f'The sum of the even-valued terms of the Fibonacci sequence is: {sum}')