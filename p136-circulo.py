# Modelamos un circulo, propiedad, radio, metodos: Area, Circunferencia
import math, os

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo[ Radio = {self.radio}, Area = {self.obtenerArea()}, Circunferencia = {self.obtenerCircunferencia()}]"
    
    # Programa principal
os.system("Cls")

circulo01 = Circulo(10.40);
print(f'El radio : {circulo01.radio}')
print(f'Area : {circulo01.obtenerArea}')
print(f'Circunferencia : {circulo01.obtenerCircunferencia}')
print()

print('Circulo 2: ')
circulo02 = Circulo(12.45)
print(circulo02)


