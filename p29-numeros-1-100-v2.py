#Imprime numeros del 1 a n usando while

import os; os.system("cls")

print("Imprime numeros del 1 al 100 usando while")

c = 1

n = int(input("Hasta donde deseas llegar?: "))

while c <= n :
    print(c, end=" ")
    c = c + 1

print("\nCiclo terminado.")