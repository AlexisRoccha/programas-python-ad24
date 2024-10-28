import os; os.system("Cls")

def dia_de_la_semana(numero):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    if 1 <= numero <= 7:
        return dias[numero - 1]
    else:
        return "No hay mas días. Introduce un número entre 1 y 7."

numero = int(input("Introduce un número entero entre 1 y 7: "))

print(f'El día de la semana correspondiente es: {dia_de_la_semana(numero)}')
