import os;

while True:
    os.system("cls")

    t = int(input("Dame la tabla que deseas imprimir?: "))
    n = int(input("Hasta donde quieres que llegue la tabla?: "))

    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")

    if input("Continuar (S/N): ").lower().startswith('n'): break

print("\nProceso terminado")