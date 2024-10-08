# p95-contar-caracteres
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
# carácter en la cadena.
# Como estrategia:
#   - Crear un diccionario donde la llave es el carácter y el valor el número de veces que aparece
#   - Hacer un ciclo que pase por cada carácter de la cadena
#       o buscamos el carácter en el diccionario, si no existe lo agregamos y sumamos 1,
#       o si ya existe solo sumamos 1

import os
os.system("cls")

cadena = input("Ingresa una cadena: ")

contador_caracteres = {}

for caracter in cadena:
    if caracter in contador_caracteres:
        contador_caracteres[caracter] += 1  # Sumar 1 si ya existe
    else:
        contador_caracteres[caracter] = 1    # Agregar al diccionario

print(contador_caracteres)