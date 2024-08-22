while True:
    nombre = input("\nHola, que tal, cual es tu nombre?: ")
    horas = float(input("Cuantas horas trabajaste: "))
    pagaxhora = float(input("A que precio te pagan la hora trabajada: "))
    tasa = 0.03
    pagatotal = (horas * pagaxhora)
    impuesto = pagatotal * tasa
    impuesto2 = pagatotal - impuesto

    print(f"El trabajador {nombre}, trabajó {horas} horas, a un precio de {pagaxhora} por hora con una tasa de {tasa}, ganando la cantidad de: {pagatotal}")
    print(f"Paga bruta: {pagatotal}")
    print(f"Impuestos: {impuesto}")
    print(f"Pago con impuestos: {impuesto2}")
