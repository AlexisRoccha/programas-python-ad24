import os; os.system("cls")

base = int(input("Base ? "))
exp = int(input("Exponente ? "))

##print(f"La base {base} elevado a la {exp} es {base ** exp}")

p = 1
for i in range(exp):
    p = p * base
print(f"La base {base} elevado a la {exp} es {base ** exp}")

p = 1
for _ in range(exp):
    p = p * base
else:
    print("El ciclo termino correctamente")
print(f"\nLa base {base} elevado a la {exp} es {base ** exp}") 
