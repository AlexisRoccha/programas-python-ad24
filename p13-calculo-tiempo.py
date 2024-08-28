'''Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos, 
   considerando que:
• 1 día tiene 24 horas,
• 1 hora tiene 60 minutos,
• 1 minuto tiene 60 segundos.'''

import os; os.system("Cls")

print("Hola, voy a convertir las horas a días, minutos y segundos.")
horas = float(input("Ingresa las horas: "))

dias = horas / 24
minutos = horas * 60
segundos = horas * 3600

print(f"Las {horas:.2f} horas transformadas a dias son: {dias:.2f} dias \nA minutos son: {minutos:.2f} minutos \nA segundos son: {segundos} segundos")
