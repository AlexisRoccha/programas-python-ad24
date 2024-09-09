'''El usuario adivina un numero entero entre 1 y 100'''

import os, random

while True:
    
    os.system("cls")  # En sistemas Windows, usa 'cls'. En Linux/Mac, usa 'clear'.
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        numero_ingresado = int(input("Adivina el número secreto (1-100): "))
        intentos += 1
        
        if numero_ingresado == numero_secreto:
            print(f"Felicidades, adivinaste el número en {intentos} intentos")
            break  # Salir del bucle una vez que adivinaste el número
        elif numero_ingresado < numero_secreto:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break  
    
print("Proceso terminado")
