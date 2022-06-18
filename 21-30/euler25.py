"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

fib = [1,1]

while len(str(fib[-1])) < 1000:
    fib.append(fib[-1]+fib[-2])

print(f'The index of the first Fibonacci number with 1000 digits is : {len(fib)}')