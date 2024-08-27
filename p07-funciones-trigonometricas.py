#Calcula las funciones trigonometricas sobre un angulo
import math as mt

print("Calcula las funciones trigonométricas sobre un ángulo")

angulod = float(input("Dame un ángulo: "))
angulor = mt.radians(angulod)

print(f"Ángulo Original: {angulod}, Ángulo en radianes: {angulor}")

salida = (f"Resumen de funciones trigonométricas\n"
          f"Seno: {mt.sin(angulor)}\n"
          f"Coseno: {mt.cos(angulor)}\n"
          f"Tangente: {mt.tan(angulor)}\n")

print(salida)
