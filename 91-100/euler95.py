"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""


def sum_of_divisors(n):
    div_sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            div_sum += i
    return div_sum

numbers = {}

for i in range(1,1000001):
    found = False
    steps = []
    num = i
    while not found:
        if num <= 1000000:
            steps.append(num)
            if num in numbers:
                for step in steps:       
                    numbers[step] = len(steps)
                found = True
            else:
                num = sum_of_divisors(num)
        else:
            for step in steps:       
                    numbers[step] = len(steps)
                    found = True
total = 0

print(max(numbers.values()))

print(f"The amount of numbers that reach 89 below 10 million are: {total}")