'''Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.'''
import os; os.system("Cls")

while True:
    n = int(input("Introduce el número hasta el cual imprimir los pares (n): "))
    
    if n > 100:
        print("El número debe ser menor o igual a 100.")
        continue  # Vuelve a pedir el número si n es mayor a 100
    
    suma_pares = 0
    i = 100  # Comienza en 100, ya que es el primer número par del rango descendente

    print(f"Números pares desde 100 hasta {n}:")
    
    while i >= n:
        if i % 2 == 0:  # Verifica si es par
            print(i, end=" ")
            suma_pares += i  # Suma el número par
        i -= 1  # Decrementa para ir hacia abajo
    
    print(f"\nSuma de los números pares: {suma_pares}")
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"):
        break

print("Fin del programa.")
