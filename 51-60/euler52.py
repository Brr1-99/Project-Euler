"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

notFound = True

i = 125874

def setNumber(n: int, x: int) -> list[int]:
    lista = [num for num in str(n*x)]
    lista.sort()
    return lista


while notFound:
    i+=1
    if setNumber(i,1) == setNumber(i,2) == setNumber(i,3) == setNumber(i,4) == setNumber(i,5) == setNumber(i,6):
        notFound = False
        break
    if len(str(i*6)) > len(str(i)):
        i = int('1'+'0'*len(str(i))) 

print(f'The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits is : {i}')
