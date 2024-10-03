import os; os.system("Cls")

nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero_mes = int(input("Introduce el número del mes (1-12): "))

nombre_mes = nombres_meses[numero_mes - 1]
dias_mes = dias_meses[numero_mes - 1]

print(f"Mes: {nombre_mes}, Días: {dias_mes}")
