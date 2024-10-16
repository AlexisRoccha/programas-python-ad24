'''Dados los siguientes números:
◦ 50,60,70,80,90,100,200
◦ 60,90,100,300,400,500
◦ 10,20,60,90,70,100,600,700
• Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
• Calcula y muestra:
◦ unión de los conjuntos A y B ( A | B )
◦ unión de los conjuntos B y C ( B | C )
◦ diferencia de A y C ( A – C)
◦ diferencia simétrica de B y C ( B ^ C)
◦ intersección de B y C ( B & C )
• Calcula y responda a las siguientes preguntas>
◦ A es subconjunto de B ?
◦ C es subconjunto de A ?
◦ 100 esta en A ?
◦ 60 esta en A , y en B y en C ?
◦ 900 no esta en C ?'''

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

union_AB = A | B
union_BC = B | C
print("\nUnion de A y B:", union_AB)
print("Union de B y C:", union_BC)

diferencia_AC = A - C
print("\nDiferencia de A menos C:", diferencia_AC)

diferencia_simetrica_BC = B ^ C
print("\nDiferencia simétrica de B y C:", diferencia_simetrica_BC)

interseccion_BC = B & C
print("Intersección de B y C:", interseccion_BC)

print("\nA es subconjunto de B:", A.issubset(B))
print("C es subconjunto de A:", C.issubset(A))

print("\n100 está en A:", 100 in A)
print("60 está en A, B y C:", 60 in A and 60 in B and 60 in C)
print("900 no está en C:", 900 not in C)
