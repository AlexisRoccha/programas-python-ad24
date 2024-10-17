'''Se desea procesar los empleados de una empresa de muebles, para lo cual deberá solicitar al
usuario los datos:
o nombre
o edad
o sexo (h/m)
o pasatiempos
o sueldo
• Los datos se pueden almacenar en una lista, cada elemento de la lista puede ser un diccionario
con los datos de un empleado.
• Al terminar la captura procesar la lista e imprimir:
o Los datos como se guardan en la lista de dicionarios
o Los datos en formato tabular
o Un resumen que incluya:
▪ Total empleados
▪ Cuantos hombres
▪ Cuantas mujeres
▪ Cunatos empleados por pasatiempo
▪ La suma de edad , promedio edad
▪ La suma de sueldo, promedio de sueldo'''

import os; os. system("cls")

print("Muebleria Muebles Dico ")
print("Sistema de Procesamiento de Empledos ")

'''Lista para almacenar los datos de los empleados'''
empleados = []

'''Pedimos los datos al usuario'''
def pedir_datos():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    sexo = input("Ingresa tu sexo (H/M): ").upper()
    pasatiempos = input("Ingresa tus pasatiempos (separados por comas): ").split(',')
    salario = float(input("Ingresa tu salario: "))
    return {
        "Nombre": nombre,
        "Edad": edad,
        "Sexo": sexo,
        "Pasatiempos": pasatiempos,
        "Salario": salario
    }

'''Pedimos datos de varios empleados'''
while True:
    empleados.append(pedir_datos())
    continuar = input("¿Deseas ingresar otro empleado? (S/N): ").upper()
    if continuar == 'N':
        break

'''Imprimimos los datos en formato de diccionarios'''
print("Datos de los empleados:")
for empleado in empleados:
    print(empleado)

'''Imprimimos los datos en formato tabular'''
print("\nTabla de datos:")
for empleado in empleados:
    print("{:<10} {:<5} {:<5} {:<10} {:<20}".format(empleado["Nombre"], empleado["Edad"], empleado["Sexo"], empleado["Salario"], ", ".join(empleado["Pasatiempos"])))

'''Resumimos los datos'''
total_empleados = len(empleados)
total_hombres = sum(1 for e in empleados if e["Sexo"] == 'H')
total_mujeres = sum(1 for e in empleados if e["Sexo"] == 'M')
suma_edades = sum(e["Edad"] for e in empleados)
promedio_edad = suma_edades / total_empleados if total_empleados > 0 else 0
suma_salarios = sum(e["Salario"] for e in empleados)
promedio_salario = suma_salarios / total_empleados if total_empleados > 0 else 0
mayor_edad = max(empleados, key=lambda e: e["Edad"])
menor_edad = min(empleados, key=lambda e: e["Edad"])

'''Contamos los pasatiempos'''
pasatiempos_contador = {}
for empleado in empleados:
    for pasatiempo in empleado["Pasatiempos"]:
        pasatiempo = pasatiempo.strip()
        if pasatiempo in pasatiempos_contador:
            pasatiempos_contador[pasatiempo] += 1
        else:
            pasatiempos_contador[pasatiempo] = 1

'''Imprimimos el resumen'''
print("\nResumen :")
print(f"Empleados: {total_empleados}")
print(f"Mujeres: {total_mujeres}")
print(f"Hombres: {total_hombres}")
print("Pasatiempos:", ", ".join(f"{k}/{v}" for k, v in pasatiempos_contador.items()))
print(f"Edad -> suma: {suma_edades}, promedio: {promedio_edad:.1f}")
print(f"Sueldo -> suma: {suma_salarios:.2f}, promedio: {promedio_salario:.2f}")
print(f"{mayor_edad['Nombre']} de {mayor_edad['Edad']} es el mayor, {menor_edad['Nombre']} de {menor_edad['Edad']} es el menor.")