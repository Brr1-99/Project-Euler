"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
 
99/70, 239/169 and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

def solution(N=1000):
  c = 0
  n = d = 1
  np = dp = 10
  for _ in range(N):
    n, d = 2 * d + n, d + n
    if n >= np:
      np*= 10
    if d >= dp:
      dp*= 10
    if np > dp:
      c+= 1
  return c

print(solution())