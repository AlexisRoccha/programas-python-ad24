'''Calcular el número mayor de una serie de números introducidos por el teclado, 
el proceso se detiene al introducir 0. El proceso debe poder repetirse hasta que el usuario lo decida.'''

import os; os.system("cls")

while True:
    mayor = None
    contador = 0

    while True:
        numero = float(input("Introduce un número (0 para terminar): "))
        contador += 1
        if numero == 0:
            break
        
        if mayor is None or numero > mayor:
            mayor = numero
    
    if mayor is not None:
        print(f"El número mayor de los {contador} numeros introducidos es: {mayor}")
    else:
        print("No se introdujo ningún número.")
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break  
print("Fin del programa.")
