"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

x = 15

y = 6

while (x + y) < 10**12:

    new_y = 2*x + y -1
    new_x = 2*new_y + x

    x, y = new_x, new_y

print(f"The number of blue balls is : {x}")
