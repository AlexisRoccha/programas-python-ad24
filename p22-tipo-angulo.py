# Muestra el tipo de angulo en base a su magnitud
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo, =360 cerrado

import os; os.system("cls")

print ("Muestra el tipo de angulo en base a su magnitud\n ")

angulo = int(input("Dame un angulo: "))

if angulo >= 0 and angulo <=360:
    print (f"\n El angulo tiene {angulo} grados, entonces es ", end="")
    if angulo <90:
        print ("Agudo")
    elif angulo==90:
        print ("Recto")
    elif angulo >90 and angulo <180:
        print ("Obtuso")
    elif angulo ==180:
        print ("Llano")
    elif angulo>180 and angulo <360:
        print ("Concavo")
    else:
        print ("Cerrado o Completo")
else:
    print ("\nEl angulo esta fuera de rango")