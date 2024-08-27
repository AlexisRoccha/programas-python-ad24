#Divide un numero entero de 3 cifras en Centenas, Decenas, Unidades

import os

os.system("Clear")

print("Divide un numero entero de 3 cifras en Centenas, Decenas, Unidades")
n = int(input("Dame un numero entero de 3 cifras: "))

c = n // 100
d = (n - (c * 100)) // 10
u = (n - (c * 100 + d * 10))


print("El numero original es: ")
print(f"Centenas: {c}")
print(f"Decenas: {d}")
print(f"Numero de la suerte: {c + d + u}")
