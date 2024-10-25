# p120-mayores-promedio - calcula el promedio de una lista, luego me regresa los que son mayores al promedio

def promedio(nums):
    s=0
    for n in nums:
        s += n
    p = s / len(nums)
    return p

def mayoresprom(nums, prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos = []
    while True:
        d = int(input("Numero: "))
        if d==-1:break
        datos.append(d)
    return datos

# Programa principal
import os; os.system("Cls")
#nums = [9,8,7.5,6,9.5,7,10,6,7]
nums = leerdatos()
print(nums)
prom = promedio(nums)
print("Promedio: ", prom)

mayprom = mayoresprom(nums, prom)
print(mayprom, len(mayprom))