# p90-crear-acceder-diccionario 
# Crear un diccionario de llave numérica dias, con los siguientes elementos:
# 1 - Lunes, 2 - Martes, 3 - Miércoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo.
#   • Muestre el diccionario.
#   • Luego, accede y muestra:
#       o El primer elemento usando []
#       o El último elemento usando []
#       o El quinto elemento usando get()
#       o El séptimo elemento usando get()
#       o Muestre el diccionario completo.

import os
os.system("Cls")

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
    }

print("Diccionario de dias:", dias)

print("\nEl primer dia es:", dias[1]) # usando []
print("El ultimo dia es:", dias[7]) # usando []
print("El quinto dia es:", dias.get(5)) # usando get()
print("El septimo dia es:", dias.get(7)) # usando get()

print("\nDiccionario completo:") 
for k, v in dias.items():
    print(f"{k} - {v}")