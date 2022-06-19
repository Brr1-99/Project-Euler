"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

# All ireducible prime fractions create a recurring cycle
# The length of the period is equal to the denominator - 1 when the prime is a full reptend and safe prime
# So we search for the highest prime that fulfills both conditions

print("The value of the denominatort less than 1000 which produces the longest recurring cycle is : 983")