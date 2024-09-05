'''Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 
1 es domingo, 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, 
mostrar un mensaje de error. Ej: 1 , Lunes, Ej 8 , dia inválido'''

import os; os.system("cls")

num = int(input("Ingresa el numero para decirte a que dia de la semana corresponde:  "))

if num == 1:
    print(f"El día correpondiente al numero {num} es el Lunes")
elif num == 2:
    print(f"El día correpondiente al numero {num} es el Martes")
elif num == 3:
    print(f"El día correpondiente al numero {num} es el Miercoles")
elif num == 4:
    print(f"El día correpondiente al numero {num} es el Jueves")
elif num == 5:
    print(f"El día correpondiente al numero {num} es el Viernes")
elif num == 6:
    print(f"El día correpondiente al numero {num} es el Sabado")
elif num == 7:
    print(f"El día correpondiente al numero {num} es el Domingo")
else:
    print("Error. Dia invalido")

