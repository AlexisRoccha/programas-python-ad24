import os; os.system('cls')

def leer_arreglo():
    entrada = input("Dame los números (separados por espacio): ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

def procesar_factoriales(lista):
    return [calcular_factorial(num) for num in lista]

numeros = leer_arreglo()
factoriales = procesar_factoriales(numeros)

print(f"\nLa lista de números originales: {numeros}")
print(f"La lista con los factoriales: {factoriales}")
