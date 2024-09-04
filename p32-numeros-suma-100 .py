# Imprime numeros hasta llegar a una suma de 100

import os; os.system("cls")

print("Imprime numeros hasta llegar a una suma de 100")

c = 0
s = 0

while c < 500:
    c = c + 1
    s = s + c
    print(c, end=" ")
    if s >= 10000:
        print("\n")
        break
    
print(f"La suma es {s}, sumando {c} numeros")
