"""
What is the largest prime factor of the number 600851475143 ?
"""


num = 600851475143
lfactor = 2

while num != 1:
    if num % lfactor == 0 :
        num /= lfactor
    else:
        lfactor+=1
        
print(f'The largest prime factor of 600851475143 is: {lfactor}')