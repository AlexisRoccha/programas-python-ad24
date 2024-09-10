'''Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
usuario lo decida.'''

import os; os.system("cls")

while True:
    n = int(input("¿Hasta qué número deseas que sea la suma de los números impares? (n): "))
    
    suma_impares = 0
    i = 1  

    print("Números impares desde 1 hasta", n, ":")
    while i <= n:
        print(i, end=" ")
        suma_impares += i
        i += 2  
    
    print("\nSuma de los números impares:", suma_impares)
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break

print("Fin del programa.")
