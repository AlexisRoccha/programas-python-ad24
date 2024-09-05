'''Dados tres números enteros, verificar cual es el mayor, ej: 10, 9 8, el mayor es 10, 11, 30,
 -1 el mayor es 30'''

import os; os.system("cls")

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a >  b and a  >  c:
    print(f"El numero {a} es mayor que el numero {b} y que el numero {c}")
elif b >  a and b  >  c:
    print(f"El numero {b} es mayor que el numero {a} y que el numero {c}")
else:
    print(f"El numero {c} es mayor que {a} y que {b}")