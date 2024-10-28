import os; os.system("Cls")

def suma_pares_impares(inicio, fin, tipo):

    if tipo == 'P':
        return sum(i for i in range(inicio, fin + 1) if i % 2 == 0)
    elif tipo == 'I':
        return sum(i for i in range(inicio, fin + 1) if i % 2 != 0)
    else:
        return "Tipo no válido. Usa 'P' para pares o 'I' para impares."

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Sumar números pares en un rango")
    print("2. Sumar números impares en un rango")
    print("3. Salir")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion in ['1', '2']:
        inicio = int(input("Introduce el número de inicio del rango: "))
        fin = int(input("Introduce el número de fin del rango: "))
        tipo = 'P' if opcion == '1' else 'I'
        resultado = suma_pares_impares(inicio, fin, tipo)
        print(f'La suma de los números {"pares" if tipo == "P" else "impares"} en el rango {inicio}-{fin} es: {resultado}')
    elif opcion == '3':
        print("¡Adiós!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print(mostrar_menu)
