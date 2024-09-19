#Imprime numeros del 100 al 1 en decrementos de 1

import os; os.system("cls")

"""print( list ( range(1, 10) ) )
print( list( range(1, 10, 2) ) )
print( list( range(1, 10, 3) ) )
print( list( range(1, 10, 3) ) )"""

for x in range(100, 0,-1):
    print(x, end=" ")