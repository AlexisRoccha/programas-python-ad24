##Calcular la paga del trabajor considerando las horas extras

import os; os.system("Cls")

print("Calcular la paga del trabajor considerando las horas extras")

nombre = input("Hola, dame tu nombre por favor: ")
horas = int(input("Horas que trabajaste?: "))
paga = float(input("Pago por hora: "))

tasa = 0.03
hextra = paganormal = pagaextra = pagabruta = 0
if horas > 40:
    hextra = horas - 40
    paganormal = 40 * paga
    pagaextra = hextra * paga * 2
    pagabruta = paganormal + pagaextra
else:
    pagabruta = horas * paga

impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"El trabajador {nombre}, trabajo {horas} horas , a una paga de: {paga:.2f} pesos")
print(f"\nHoras extra     : {hextra}, Paga normal: {paganormal}, Pago extra: {pagaextra}")
print(f"\nPaga bruta      :{pagabruta:.2f}")
print(f"\nImpuestos       :{impuesto:.2f}")
print(f"\nPaga neta       :{paganeta:.2f}")
