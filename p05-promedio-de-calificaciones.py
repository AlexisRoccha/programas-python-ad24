print("Hola, introduce tus tres calificaciones para calcular el promedio.")
print("Introduce las 3 califiaciones enteras separadas por un espacio ")

c1, c2, c3 = input().split()
c1, c2, c3 = int(c1), int(c2), int(c3)

suma = ( c1 + c2 + c3 )
prom = (c1 + c2 + c3) / 3

print(f"Las calificaciones fueron: {c1}, {c2}, {c3}")
print(f"La suma fue: {suma}")
print(f"El promedio de las 3 calificaciones fueron: {prom}")

