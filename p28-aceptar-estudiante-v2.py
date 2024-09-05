'''Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. 
La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.
Ej: Maria, 22, M, 10 9 10, Maria has sido aceptada, tu edad de 22 y tus calificaciones 10, 9 y 10, lo permiten
Ej: Jose, H, 21, 7, 6, 5, solo aceptamos mujeres
Ej: Dolores, M ,20, 10, 10, 10, Eres mujer, pero no tienes la edad, solo mayores a 21
Ej: Sandra, M, 25, 7, 6, 5, Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5'''

import os
os.system("cls")

nombre = input("Hola, ingresa tu nombre por favor: ").capitalize()  # Convertir la primera letra en mayúscula
sexo = input("Ahora ingresa tu sexo si es M o H: ").upper()  # Convertir a mayúscula

if sexo == "H":
    print(f"{nombre}, lo sentimos, solo aceptamos mujeres.")
    exit()  # Terminar el programa inmediatamente si es hombre

edad = int(input("Ingresa ahora tu edad: "))
cuno = float(input("Ingresa la primera calificación: "))
cdos = float(input("Ingresa la segunda calificación: "))
ctres = float(input("Ingresa la tercera calificación: "))

promca = (cuno + cdos + ctres) / 3  # Calcular el promedio

if sexo == "M" and edad < 21 and promca >= 8:
    print(f"{nombre}, eres mujer, pero lo sentimos. Tu edad de {edad} no nos permite aceptarte.")
elif sexo == "M" and edad < 21 and promca < 8:
    print(f"{nombre}, eres mujer, pero lo sentimos. Tu edad de {edad} y tu calificación de {promca:.2f} es menor a la que aceptamos.")
elif sexo == "M" and edad >= 21 and promca < 8:
    print(f"{nombre}, eres mujer, pero lo sentimos. Tu edad de {edad} es correcta, pero tu calificación de {promca:.2f} es menor a la que aceptamos.")
else:
    print(f"{nombre}, ¡felicidades! Fuiste aceptada. Tu edad de {edad} años y tu calificación final de {promca:.2f} lo permiten.")
