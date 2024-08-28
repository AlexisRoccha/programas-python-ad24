'''Dada una temperatura en grados Celsius, obtener su equivalente en grados farenheit, 
   usando la siguiente formula:
   farenheit = (celcius × 9/5) + 32'''

import os; os.system("Cls")

print("Hola, para convertir la temperatura es necesario que nos des los siguientes valores...")
temp = float(input("Ingresa los grados Celsius para convertir a Farenheit: "))

farenheit = (temp * 9/5) + 32

print(f"Los {temp} grados Celsius a Farenheit son: {farenheit:.2f}")
