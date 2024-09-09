#Imprime numeros del 1 al 100 usando while

import os; os.system("cls")

print("Imprime numeros del 100 al 1 usando while")

n = int(input("Hasta donde deseas llegar?: "))
c = n

while c >= 1 :
    print(c, end=" ")
    c = c - 1

print("\nCiclo terminado.")