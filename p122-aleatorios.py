# genera 2 listas de numeros aleatorios

def generar_aleatorios(n):
    lista=[]
    for i in range(n+1):
        lista.append(random.randint(1,100))
    return lista

def suma_lista(lista1,lista2, n):
    lista3 = []
    for i in range(n):
        lista3.append( lista1(i) + lista2(i))
    return lista3

# Programa principal
MAX = 10
import os, random; os.system('cls')

nums1 = generar_aleatorios(MAX)
nums2 = generar_aleatorios(MAX)
nums3 = generar_aleatorios(MAX)

print('Lista 1 ', nums1)
print('Lista 2 ', nums2)
print('Lista 3 ', nums3)
