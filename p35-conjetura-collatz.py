'''Calcula o imprime los numeros de la conjetura de collatz'''

import os; os.system("cls")

while(True):
    num = int(input("Dame un entero positivo?: "))

    while num!=1 :
        print(num, end= " ")
        if num % 2 == 0 :
            num = num // 2
        else:
            num = num * 3 + 1
    print(num, end=" ")


    if input("\n¿Deseas continuar (S/N)?:").upper().startswith("N") : break
print("Proceso terminado.")