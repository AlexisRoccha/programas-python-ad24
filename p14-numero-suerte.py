'''Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la 
suerte. Mostrar los dígitos individuales y el número de la suerte.'''

import os; os.system("Cls")

print("Hola, hoy te daré tu numero de la suerte basandome en la suma de los numeros individuales de la fecha de nacimiento.")
fecha = int(input("Ingresa por favor tu fecha de nacimiento para conocer tu numero de la suerte: "))

mil = fecha // 1000        
cien = (fecha // 100) % 10  
dec = (fecha // 10) % 10    
uni = fecha % 10 

numero_de_la_suerte = mil + cien + dec + uni
print(f"Los dígitos individuales de tu año de nacimiento son: \n{mil} \n{cien} \n{dec} \n{uni}")
print(f"Tu número de la suerte es: {numero_de_la_suerte}")