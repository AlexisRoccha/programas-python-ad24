import os; os.system("Cls")

import math

def leer_arreglo():
    nums = input("Dame los números separados por espacios: ").split()
    lista = [int(num) for num in nums]
    return lista

def mayor(lista):
    valor_maximo = lista[0]
    for num in lista:
        if num > valor_maximo:
            valor_maximo = num
    return valor_maximo

def menor(lista):
    valor_minimo = lista[0]
    for num in lista:
        if num < valor_minimo:
            valor_minimo = num
    return valor_minimo

def media(lista):
    suma_total = sum(lista)
    return suma_total / len(lista)

def varianza(lista):
    m = media(lista)
    suma_diferencias = sum((x - m) ** 2 for x in lista)
    return suma_diferencias / len(lista)

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista))

# Programa principal
numeros = leer_arreglo()

med = media(numeros)
may = mayor(numeros)
men = menor(numeros)
var = varianza(numeros)
desv_est = desviacion_estandar(numeros)

print(f"\nLista de números: {numeros}")
print(f"La media: {med:.3f}")
print(f"Mayor de los datos: {may}")
print(f"Menor de los datos: {men}")
print(f"Varianza: {var:.3f}")
print(f"Desviación estándar: {desv_est:.3f}")
