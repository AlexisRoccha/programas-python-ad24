'''Leer n nombres de ciudades en una lista hasta introducir $
• Imprimir cuantos elementos son, y la lista completa
• Ordenar la lista en orden descendente y mostrar (sort)
• Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres'''

import os; os.system("cls")

ciudades = []
while True:
    ciudad = input("Introduce el nombre de una ciudad (o $ para terminar): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)

print(f"Cantidad de ciudades: {len(ciudades)}")
print("Lista de ciudades:", ciudades)

ciudades.sort(reverse=True)
print("Lista de ciudades en orden descendente:", ciudades)

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ciudades_consonantes = [ciudad for ciudad in ciudades if ciudad[0] in consonantes]
print(f"Cantidad de ciudades que comienzan con una consonante: {len(ciudades_consonantes)}")
print("Ciudades que comienzan con una consonante:", ciudades_consonantes)
