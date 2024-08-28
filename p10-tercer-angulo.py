'''import math as math'''
import os; os.system("Cls")

print(("Hola, para conocer el angulo faltante ingresa los angulos conocidos"))
angulo1 = float(input("Ingresa el primer angulo: "))
angulo2 = float(input("Ingresa el segundo angulo: "))

angulo3 = 180 - (angulo1 + angulo2)
print(f"Valor del angulo 1: {angulo1} \nValor del angulo 2: {angulo2} \nLa medida del angulo 3 es: {angulo3}")

