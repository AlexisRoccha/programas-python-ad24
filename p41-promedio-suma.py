'''Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
decida.'''

import os; os.system("cls")


while True:
    suma = 0
    contador = 0
    
    numero = float(input("Introduce un número (0 para terminar): "))
    
    while numero != 0:
        suma += numero
        contador += 1
        numero = float(input("Introduce un número (0 para terminar): "))
    
    if contador > 0:
        promedio = suma / contador
        print("Suma:", suma)
        print("Promedio:", promedio)
        print("Cantidad de números introducidos:", contador)
    else:
        print("No se introdujeron números.")
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break  
print("Fin del programa.")

    
