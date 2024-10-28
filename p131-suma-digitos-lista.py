import os; os.system("Cls")

def obtener_numeros():
    numeros = list(map(int, input("Dame los números separados por espacios: ").split()))
    return numeros

def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma

def calcular_sumas(lista):
    return [suma_digitos(num) for num in lista]

numeros = obtener_numeros()
sumas_digitos = calcular_sumas(numeros)

print("\nLista de números original:", numeros)
print("Lista con la suma de los dígitos:", sumas_digitos)
