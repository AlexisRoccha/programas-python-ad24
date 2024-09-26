'''Se desea imprimir los pares de 2 a n y su suma'''

import os; os.system("cls")

suma = 0

n = int(input("Dame número: "))


for i in range(2, n + 1, 2): 
    print(i, end=" ")
    suma += i
print(f"\nLa suma de los números pares es: {suma}")