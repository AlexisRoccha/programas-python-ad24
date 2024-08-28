'''Se desea calcular el volumen de un cilindro dado su radio y altura, 
   usando la siguiente formula:
• Volumen = PI * (Radio * Radio) * Altura'''

import os; os.system("Cls")
import math as mt

print("Para conocer el volumen del cilindro es necesario conocer las siguientes medidas:")
radio = float(input("Radio: "))
altura = float(input("Altura: "))

volumen = mt.pi * (radio * radio) * altura
print(f"Dado el radio que es: {radio} y la altura: {altura}, el volumen del cilindro es: {volumen:.2f}")



