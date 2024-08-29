#Verificar si la suma de dos numeros es igual a un tercero
import os; os.system("Cls")

print("Verifica si la suma de dos numeros es igual a un tercero\n")

n1 = int(input("Dame numero 1: "))
n2 = int(input("Dame numero 2: "))
n3 = int(input("Dame numero 3: "))

if n1 + n2 == n3:
    print("Son iguales")
else:
    print("Son diferentes")
    print("Proceso terminado.")