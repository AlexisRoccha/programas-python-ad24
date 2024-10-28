import os; os.system("Cls")

def menor():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = int(input("Introduce el tercer número: "))
    
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

menor = menor()
print("El número menor es:", menor)
