'''Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
final. El proceso debe poder repetirse hasta que el usuario lo decida.'''

import os; os.system("cls")

while True:
    temp_inicial = int(input("Introduce la temperatura inicial en grados centígrados: "))
    temp_final = int(input("Introduce la temperatura final en grados centígrados: "))

    print("\nConversión de grados centígrados a Fahrenheit en proceso...")
    
    temp_c = temp_inicial  # Inicializamos la temperatura actual
    while temp_c <= temp_final:
        temp_f = (temp_c * 9/5) + 32
        print(f"{temp_c}°C = {temp_f:.2f}°F")
        temp_c += 1  # Incrementa la temperatura en 1
    
    if input("¿Deseas continuar (S/N)?: ").upper().startswith("N"): break  

print("Fin del programa.")
