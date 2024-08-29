'''Verificar si un numero es positivo, negativo o cero'''

import os; os.system("Cls")

print("Verificar si un numero es positivo, negativo o cero\n")
numero = int(input("Dame un numero entero: "))

if numero > 0:
    print("El numero es positivo.")

elif numero < 0:
    print("El numero es negativo.")

else:
    print("El numero es cero")
    
print("Proceso terminado...")