"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

first_year = [2,5,5,1,3,6,1,4,7,2,5,7]

sundays = 3

for i in range (1,101):
    if i%4 != 0:
        for num in first_year:
            num += 1
            num = num%7
            if num == 7 or num == 0:
                sundays += 1
    else:
        for num in first_year:
            num += 2
            num = num%7
            if num == 7 or num == 0:
                sundays += 1

print(f'The number of Sundays that fall on the first of the month during the twentieth century is: {sundays}')