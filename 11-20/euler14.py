"""
Given the Collatz sequence.
Which starting number, under one million, produces the longest chain?
"""

numbers = {1: 1}

max_steps = 1

number = 1

way = 0

def steps(n: int) -> int:
    global way
    if n in numbers:
        way += numbers[n]
        return way
    else:
        if n % 2 == 0:
            way += 1
            return steps(int(n/2))
        else :
            way += 1
            return steps(int(3*n + 1))

n = 2
while n < 1000000:
    new_steps = steps(n)
    numbers[n] = new_steps
    if new_steps > max_steps:
        number = n
        max_steps = new_steps
    n += 1
    way = 0

print(f'The number that produces the longest chain is : {number} , with a number of steps of {max_steps}')