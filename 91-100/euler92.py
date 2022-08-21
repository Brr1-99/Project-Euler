"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

"""

def next_iteration(num: int) -> int:
    return sum(int(d)**2 for d in str(num))

numbers = {
    1: 1,
    89: 89,
    }

for i in range(1,10000001):
    found = False
    steps = []
    num = i
    while not found:
        steps.append(num)
        if num in numbers:
            for step in steps:       
                numbers[step] = numbers[num]
            found = True
        else:
            num = next_iteration(num)

total = 0

for value in numbers.values():
    if value == 89:
        total += 1

print(total)