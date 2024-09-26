'''Se desea imprimir los números de 1 a n de 10 en 10'''
import os; os.system("cls")


n = int(input("Dame el numero que quieres que te imprima de 10 en 10?: "))

for i in range(1, n + 1, 10):
    print(i, end=" ")