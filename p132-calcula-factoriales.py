import os; os.system("Cls")

def procesar_numeros(): 
    numeros = list(map(int, input("Dame los números separados por espacio: ").split()))

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    
    factoriales = [factorial(num) for num in numeros]

    print("La lista de números originales:", numeros)
    print("La lista con los factoriales:", factoriales)

procesar_numeros()
