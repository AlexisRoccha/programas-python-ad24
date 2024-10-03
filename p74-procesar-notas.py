'''Leer n notas hasta introducir un 0
• Las notas pueden estar entre 0 y 100 (validar)
• Imprime:
◦ cuantas notas, las notas,
◦ suma, promedio,
◦ notas menores al promedio y cuantas son
◦ nota máxima y nota mínima'''

import os


os.system("cls")

notas = []

while True:
    nota = float(input("Introduce una nota (0 para terminar): "))
    if nota == 0:
        break
    if 0 <= nota <= 100:
        notas.append(nota)
    else:
        print("Nota inválida. Debe estar entre 0 y 100.")

cantidad = len(notas)
suma = sum(notas)
promedio = suma / cantidad if cantidad > 0 else 0
menores_promedio = [nota for nota in notas if nota < promedio]
max_nota = max(notas) if notas else None
min_nota = min(notas) if notas else None

print(f"Cantidad de notas: {cantidad}")
print(f"Notas: {notas}")
print(f"Suma de las notas: {suma}")
print(f"Promedio de las notas: {promedio}")
print(f"Notas menores al promedio: {menores_promedio}")
print(f"Cantidad de notas menores al promedio: {len(menores_promedio)}")
print(f"Nota máxima: {max_nota}")
print(f"Nota mínima: {min_nota}")
