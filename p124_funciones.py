def leerdatos():

    datos = []
    while True:
        d = int(input('Numero ?'))
        if d ==-1: break
        datos.append(d)
    return datos

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

