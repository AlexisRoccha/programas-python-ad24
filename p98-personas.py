'''• Dados los siguientes nombres:
• Juan, Maria, Pedro, Jose, Rocio
• Pedro, Juan, Pablo, Mateo, Esther
• Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )
• Calcula y muestra:
◦ union de los conjuntos ( A | B)
◦ intesección de los conjuntos ( A & B)
◦ diferenia de los conjuntos ( A - B )
◦ diferencia simetrica de los conjuntos ( A ^ B )
• Calcula y muestra también
◦ si el conjunto de nombres Pablo, Mateo, es subconjunto de B
◦ si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica
◦ si Pedro esta en A
◦ si Lilia no esta en B'''

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print("Conjunto A:", A)
print("Conjunto B:", B)

union = A | B
print("\nUnion de A y B:", union)

interseccion = A & B
print("Intersección de A y B:", interseccion)

diferencia = A - B
print("Diferencia de A menos B:", diferencia)

diferencia_simetrica = A ^ B
print("Diferencia simétrica de A y B:", diferencia_simetrica)

subconjunto = {"Pablo", "Mateo"}
print("\nPablo y Mateo es subconjunto de B:", subconjunto.issubset(B))

superconjunto = {"Reynaldo", "Angelica"}
print("A es superconjunto de Reynaldo y Angelica:", A.issuperset(superconjunto))

print("\nPedro está en A:", "Pedro" in A)
print("Lilia no está en B:", "Lilia" not in B)
