"""
What is the sum of the digits of the number 2**1000?
"""

number = [2]

i=1
while i < 1000:
    for j in range(len(number)):
        number[j] *= 2
    greater_10 = [num for num in number if num >= 10]
    while len(greater_10) != 0:
        for j in range(len(number)):
            if number[j] >= 10:
                number[j] = number[j] % 10 
                try:
                    number[j+1] += 1
                except:
                    number.append(1)
        greater_10 = [num for num in number if num >= 10]
    i+=1
print(f'The sum of de digits of 2**1000 is : {sum(number)}')


sum = 0
for n in str(2**1000):
	sum += int(n)
print (sum)