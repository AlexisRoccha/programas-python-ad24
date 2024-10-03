'''Leer dos listas con 5 elementos
• Multiplica las listas y guárdalos en una tercera lista
• Imprime las tres listas'''

import os; os.system("cls")

lista1 = [int(input(f"Introduce el elemento {i+1} de la lista 1: ")) for i in range(5)]
lista2 = [int(input(f"Introduce el elemento {i+1} de la lista 2: ")) for i in range(5)]

lista3 = [lista1[i] * lista2[i] for i in range(5)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (resultado de la multiplicación):", lista3)
