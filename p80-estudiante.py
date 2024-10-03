'''Datos de un estudiante usando un diccionario'''

import os; os.system("Cls")

estudiante = { "Nombre" : "Juan Perez",
                "Edad"  : 45,
                "Correo" : "jperez@msn.com",
                "Carrera" : "Sistemas" }

print(f"El estudiante" , estudiante, len(estudiante))

estudiante["calificacion"] = 9.5
estudiante["Correo"] = "juanp@gmail.com"
print("El estudiante ", estudiante, len(estudiante))

print("\nLlaves ", estudiante.keys())
for k in estudiante.keys():
    print(k,end=" ")

print("\nValores ", estudiante.values())
for v in estudiante.values():
    print(v,end=" - ")

print("\nLlaves y valores al mismo tiempo")
for k, v in estudiante.items():
    print("{k:<15} : {v}")

print("\nLlaves y valores al mismo tiempo - forma 2")
for k in estudiante.keys():
    print(f"{k:<15} : {estudiante[k]}")
