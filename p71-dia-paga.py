'''MUESTRA LA PAGA SEGUN EL DIA DE LA SEMANA, USANDO DOS LISTAS'''

import os; os.system("Cls")

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"].upper()
paga = [100, 200, 300, 400, 500, 600, 700]

dia = " "
while True:
    dia = input("Dia?:")
    if dia in dias:
        break
print("Dia", dia)
pos = dias.index(dia)
print("La paga ", paga[pos])
