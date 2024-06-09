"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def check_bouncy(num) -> bool:
    nums = [int(x) for x in str(num)]
    if nums == sorted(nums, reverse=False) or nums == sorted(nums, reverse=True):
        return False
    else:
        return True

total_num = 21780

bouncy = total_num * 0.9

percentage = bouncy/ total_num * 100

while percentage < 99:
    total_num += 1
    if check_bouncy(total_num):
        bouncy +=1
    percentage = bouncy/ total_num * 100

print(total_num)
