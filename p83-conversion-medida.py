import os; os.system("cls")

conversiones ={
    "Km" : 1000,
    "m" : 1,
    "cm" : 0.01,
    "mm" : 0.001
}
longitud = int(input("Longitud: "))

while True:
    print("Unidades : ", conversiones.keys())
    unidad = input()
    if unidad in conversiones:
        break

resultado = longitud * conversiones[unidad]

print(f"Longitud: {longitud} {unidad} son {resultado} metros")
