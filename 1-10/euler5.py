import math
"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
i = 0
mcm = 1
nums = [2,3,5,7,11,13,17,19,21]
a = [1,1,1,1,1,1,1,1]
k = 20
check = True
limit = math.sqrt(20)

while nums[i] <= k:
    a[i] = 1
    if check :
        if nums[i] <= limit:
            a[i] = math.floor(math.log(k)/math.log(nums[i]))
        else:
            check = False
    mcm*= nums[i]**a[i]
    i+=1

print(f'The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {mcm}')