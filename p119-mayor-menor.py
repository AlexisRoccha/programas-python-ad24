# Dada una lista de numeros introducidos por el usuario, regresar el mayor y el menor
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

# Programa Principal
import os; os.system("Cls")
nums = leerdatos()
print(nums)
may = mayor(nums)
men = menor(nums)
print('El mayor es ', may)
print('El menor es ', men)