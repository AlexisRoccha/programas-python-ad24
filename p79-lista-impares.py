import os; os.system("cls")

n = int(input("Introduce el valor de n: "))

impares = [i for i in range(1, 2*n, 2)]
print("Lista de números impares:", impares)

suma = sum(impares)
promedio = suma / len(impares)
print("Suma de los números impares:", suma)
print("Promedio de los números impares:", promedio)

divisibles_por_3 = [num for num in impares if num % 3 == 0]
suma_divisibles_por_3 = sum(divisibles_por_3)
print("Números divisibles entre 3:", divisibles_por_3)
print("Suma de los números divisibles entre 3:", suma_divisibles_por_3)

elemento_a_buscar = int(input("Introduce el número a buscar en la lista: "))
if elemento_a_buscar in impares:
    posicion = impares.index(elemento_a_buscar)
    print(f"El número {elemento_a_buscar} está en la lista en la posición {posicion}.")
else:
    print(f"El número {elemento_a_buscar} no está en la lista.")
