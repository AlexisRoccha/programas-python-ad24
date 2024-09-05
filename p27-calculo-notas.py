'''Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado 
e imprimir un mensaje de acuerdo al promedio obtenido:'''

import os; os.system("cls")

prim = float(input("Ingresa la primera calificación: "))
segu = float(input("Ingresa la segunda calificación: "))
terc = float(input("Ingresa la tercera calificación: "))
cuar = float(input("Ingresa la cuarta calificación: "))
quint = float(input("Ingresa la quinta calificación: "))

prom = (prim + segu + terc + cuar + quint) / 5

if prom >= 0 and prom <= 6:
    print("Quedas reprobado")
elif prom > 6 and prom <= 7:
    print("Pasas de panzazo")
elif prom > 7 and prom <= 8:
    print("Muy bien, puedes mejorar")
elif prom > 8 and prom <= 9:
    print("Excelente sigue así")
else:
    print("PERFECTO, TU ESFUERZO Y DESVELADAS VALIERON LA PENA")

