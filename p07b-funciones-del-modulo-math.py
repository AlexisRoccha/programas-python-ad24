import math as mt

w = 10.34
x = 10
y = 20
z = 30

print(f"Los numeros son: {x}, {y}, {z}")
print(f"Maximo comun divisor: {mt.gcd(x,y,z)}")
print(f"Valor Maximo: {max(x,y,z)} ")
print(f"Valor Minimo: {min(x,y,z)} ")
print(f"Elevar a una potencia: {mt.pow(x,y)}")

print(f"Redondear hacia arriba: {mt.ceil(w)}")
print(f"Redondear hacia abajo: {mt.floor(w)}")
print(f"Redondear: {round(w)}")
print(f"Sin decimales(truncar): {mt.trunc(w)}")

