import os; os.system("Cls")

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

def mostrar_menu():
    print("Seleccione una opción de conversión:")
    print("1. Pulgadas a centímetros")
    print("2. Metros a pies")
    print("3. Salir")

    opcion = input("Elige una opción (1/2/3): ")
    
    if opcion == '1':
        pulgadas = float(input("Introduce las pulgadas: "))
        print(f'{pulgadas} pulgadas son {pulgadas_a_centimetros(pulgadas)} cm.')
    elif opcion == '2':
        metros = float(input("Introduce los metros: "))
        print(f'{metros} metros son {metros_a_pies(metros)} pies.')
    elif opcion == '3':
        print("¡Adiós!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print(mostrar_menu)
