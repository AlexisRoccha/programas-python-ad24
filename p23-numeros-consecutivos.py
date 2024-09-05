'''Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, 
si no lo son (1,4,6) mandar mensaje de error.'''

import os; os.system("cls")

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a + 1 == b and b + 1 == c:
    print("Los números son consecutivos.")
else:
    print("Error: los números no son consecutivos.")