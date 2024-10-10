# Procesar un pedido de pizza usando diccionarios en Python

import os; os.system("Cls")

ings = {
    'T' : 1.50,
    'P' : 3.50,
    'C' : 3.74,
    'A' : 0.40
}

st = 0
base = 15
tot = 0
des = 0

pedido = input('Que ingredientes deseas para tu pizza?: ').upper()

for ing in ings:
    if ing in 'TPCA':
        st += ings[ing]

des = (st * 0.05)
st = st + base

if st >= 20:
    tot = st - (st * des)


print(f'El subtotal es {st:.2f}')
print(f'El total es {tot:.2f}')
print(f'El descuento es de {des:.2f}')
