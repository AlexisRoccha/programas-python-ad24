import os; os.system("Cls")

def leer_arreglo():
    entrada = input("Ingresa los números (separados por espacio): ")
    return [int(num) for num in entrada.split()]

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def suma_digitos_lista(lista):
    resultado = []
    for num in lista:
        resultado.append(suma_digitos(num))
    return resultado

# Programa principal
numeros = leer_arreglo()
resultado_suma_digitos = suma_digitos_lista(numeros)

print(f"\nLa lista de números original: {numeros}")
print(f"La lista con las sumas de los dígitos: {resultado_suma_digitos}")
