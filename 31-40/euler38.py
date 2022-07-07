"""
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import count

def ispandigital(n: int) -> bool:
   digits = str(n)
   for i in count(2):
      ndig = len(digits)
      if ndig < 9: 
        digits += str(n * i)
      elif ndig == 9 and set(digits) == set('123456789'):
         return int(digits)
      else: 
        return False

print (max(map(ispandigital, range(1, 10000))))