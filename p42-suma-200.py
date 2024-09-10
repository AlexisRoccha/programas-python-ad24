'''Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, 
luego mostrar cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse 
hasta que el usuario lo decida.'''

import os; os.system("cls")

while True:
        
        suma = 0
        contador = 0
        
        while suma < 200:
            numero = float(input("Introduce un número: "))
            suma += numero
            contador += 1
        
        print("Suma total:", suma)
        print("Cantidad de números introducidos:", contador)
        
        if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break  
print("Fin del programa.")