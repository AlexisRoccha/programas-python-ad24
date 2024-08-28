'''Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes 
   de sus lados, usando la
siguiente formula: hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )'''
import math as mt
import os; os.system("Cls")

lado1 = float(input("Hola, para conocer la hipotenusa ingresa el valor del lado 1: "))
lado2 = float(input("Ingresa el valor del lado 2: "))

hipotenusa = mt.sqrt((lado1 * lado1) + (lado2 * lado2)) 
print(f"Dado el lado 1 que vale: {lado1} \nValor del lado 2: {lado2} \nEl valor de la hipotenusa es: {hipotenusa:.2f}")