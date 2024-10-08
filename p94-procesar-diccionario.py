# p94-procesar-diccionario
# • Se tienen los datos de nombres y sueldos de los siguientes trabajadores, en dos listas:
# Nombres: Juan, Pedro, Manuel, Elias, Maria, Felipe, Julia, Roberto
# Sueldos: 4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00
#   • Crear un diccionario con ambas listas
#   • Mostrar el diccionario resultante
#   • Iterar por los elementos del diccionario:
#       o Usando las llaves : keys()
#       o Usando los valores: values()
#       o Usando la llave y el valor en base a la llave
#       o Usando el para llave/valor items()
#   • Obtener lo suma de los sueldos
#    • Obtener el promedio de los sueldos.

import os
os.system("cls")

nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

trabajadores = dict(zip(nombres, sueldos))

print("Diccionario de trabajadores:", trabajadores)

print("\nNombres de los trabajadores:")
for nombre in trabajadores.keys(): # Iterar usando las llaves
    print(nombre)

print("\nSueldos de los trabajadores:")
for sueldo in trabajadores.values(): # Iterar usando los valores
    print(sueldo)

print("\nNombres y sueldos:")
for nombre in trabajadores: # Iterar usando la llave y el valor en base a la llave
    print(f"{nombre}: {trabajadores[nombre]}") 

print("\nNombres y sueldos usando items():")
for nombre, sueldo in trabajadores.items():  # Iterar usando items()
    print(f"{nombre}: {sueldo}")

suma_sueldos = sum(trabajadores.values())
print(f"\nSuma de los sueldos: {suma_sueldos}")

promedio_sueldos = suma_sueldos / len(trabajadores)
print(f"Promedio de los sueldos: {promedio_sueldos}")