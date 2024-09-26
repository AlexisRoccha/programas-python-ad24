'''Se desea imprimir la secuencia de términos armónicos el numero de renglones 
que el usuario desee y su suma:'''

import os
import math

os.system("cls")

n = int(input("¿Cuántos términos?: "))

suma = 0  

for i in range(1, n + 1):
    termino = 1 / math.factorial(i)
    suma += termino
    
    if i == 1:
        print("1", end="")
    else:
        print(f" + 1/{i}!", end="")

print(f" suma: {suma}")