import os; os.system("cls")

while True:

    print("[1] Imprimir numeros pares de n a 2")
    print("[2] Imprimir numeros impares de 1 a n")
    print("[3] Salir")

    op = int(input("Elige ? "))

    if op ==1:
        s = 0
        print("Imprimiendo numeros pares de n a 2")
        n = int(input("Desde dónde? "))
        n = n if n%2==0 else n-1
        for x in range(n, 1, -2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de pares es " + str(s))
    elif op ==2:
        s = 0
        print("Imprimiendo numeros impares de 1 hasta n")
        n = int(input("Hasta donde?: "))
        n = n if n%2!=0 else n-1
        for x in range(1, n+1, 2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de numeros impares es " + str(s))
    elif op ==3:
        break
    else: 
        print("\nOpcion invalida")

    input("\n< Presiona cualquier tecla para contuinuar >")