from decimal import Decimal, getcontext

getcontext().prec = 10000000

suma = 0

for i in range(1, 100 + 1):
    print(i)
    num = Decimal(1/i)
    try:
        suma += int(str(num).split('.')[1][i-1])
    except Exception as e:
        suma += 0



print(suma)