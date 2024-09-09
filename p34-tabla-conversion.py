'''Imprimir una tabla de conversion de pesos a dolares'''
while(True):
    import os; os.system("cls")

    tc = 19.87

    while(True):
        pi = float(input("Valor en pesos iniciales: "))
        pf = float(input("Valor en pesos final: "))
        if pi <  pf :
            break
    c = pi

    print("\nPeso\tDollar")
    while c <= pf :
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)

    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N") : break 

   