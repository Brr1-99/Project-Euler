"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
a, b = 100, 100
palindrome = 10000
for i in range (100,1000):
    for j in range(100,1000):
        mult = i*j
        string = str(mult)
        if (string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3]) and mult > palindrome:
            a,b = i,j
            palindrome = mult
print(f"The largest palindrome made from the product of two 3-digit numbers is: {palindrome}. \nThose two numbers are: {a} and {b}.")