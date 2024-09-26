'''Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:'''

import os;

os.system("cls")

r = int(input("Dame numero? "))


for i in range(1, r+1):
    for j in range(1, i+1):
        print(j, end="")
    print()