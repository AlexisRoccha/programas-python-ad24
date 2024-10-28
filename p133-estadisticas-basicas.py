def estadisticas(lista):
    media = sum(lista) / len(lista)
    mayor = max(lista)
    menor = min(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    desviacion_estandar = varianza ** 0.5
    return media, mayor, menor, varianza, desviacion_estandar

numeros = list(map(int, input("Dame números separados por espacio: ").split()))

media, mayor, menor, varianza, desviacion_estandar = estadisticas(numeros)

print("Lista de números:", numeros)
print("La media:", media)
print("Mayor de los datos:", mayor)
print("Menor de los datos:", menor)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion_estandar)
