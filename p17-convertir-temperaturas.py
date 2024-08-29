##Convertir temperatura de Celcius a Farentheit y viceversa

import os; os.system("Cls")
print("Convertir temperatura de Celcius a Farentheit y viceversa")
print("[ 1 ] Convertir de Farentheit a Centigrados")
print("[ 2 ] Convertir de Centigrados a Farentheit")
print("[ 3 ] Salir")

op = int(input("Escoge la opción que quieras: "))

if op == 1:
    print("Convirtiendo de Farentheit a Centigrados")
    temp =float(input("Dame los grados Farentheit: "))
    resp = (temp - 32) * 5 / 9
    print(f"{temp} Farentheit equivale a {resp:.2f} Centigrados")
elif op == 2:
    print("Convirtiendo de Celcius a Farentheit")
    temp =float(input("Dame los grados Centigrados: "))
    resp = (temp * 9 / 5) + 32
    print(f"{temp} Centigrados equivale a {resp:.2f} Farentheit")
elif op == 3:
    print("Te vas porque tu quieres")
else:
    print("Opcion erronea.")


